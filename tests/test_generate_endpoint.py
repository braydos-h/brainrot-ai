import os
import sys
import io
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


class DummyProcess:
    """A minimal stand-in for subprocess.Popen used in testing."""

    def __init__(self, output: str):
        self.stdout = io.StringIO(output)

    def wait(self):
        return 0


def test_generate_endpoint():
    dummy_text = "generated line\n"
    with patch("subprocess.Popen", return_value=DummyProcess(dummy_text)) as mock_popen:
        with app.test_client() as client:
            response = client.post("/generate", json={"prompt": "hi"})

            assert response.status_code == 200
            assert dummy_text.strip() in response.get_data(as_text=True)

        mock_popen.assert_called_once()
        args = mock_popen.call_args[0][0]
        assert args[:3] == ["ollama", "run", "qwen2.5:1.5b"]

