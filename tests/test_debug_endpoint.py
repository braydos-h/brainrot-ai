import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app


def test_debug_endpoint():
    with app.test_client() as client:
        response = client.get('/debug')
        assert response.status_code == 200
        data = response.get_json()
        assert 'cpu_usage' in data
        assert 'ram_usage' in data
        assert 'disk_usage' in data
        assert 'ping' in data
        assert 'wifi' in data
