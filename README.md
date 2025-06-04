# IGOON.ORG-AI

This is a Flask web app that connects to a local [Ollama](https://ollama.com) LLM backend and lets users chat in different styles—ranging from full-on "nerd mode" to unhinged "max brainrot."

## ✨ Features

- **🌐 Web Interface**  
  Simple, responsive Flask frontend (`index.html`, `chat.html`, `boot.html`).

- **🧠 Persona Modes**  
  Choose how the LLM responds:
  - **Nerd Mode**: Precise, technical, short.
  - **Brainrot Mode**: Chaotic lowercase slang with emojis.
  - **Max Brainrot**: Emotionally decayed, grammatically broken rot-core.

- **💬 Live Chat Generation**  
  Prompts are streamed directly from `ollama run qwen2.5:1.5b` for real-time response.

- **🧪 Debug Panel**  
  Check system stats at `/debug`:
  - CPU, RAM, disk usage
  - Ping latency
  - Wi-Fi connection status

- **♻️ Clear History**  
  Reset the chat anytime via `/clear`.

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/braydos-h/IGOON.ORG-AI
cd multi-persona-chat
```

### 2. Install Dependencies

```bash
pip install flask psutil pytest
```

### 3. Run the App

```bash
python app.py
```

## Running Tests

Use `pytest` to run the test suite:

```bash
pytest
```

## License

This project is licensed under the [MIT License](LICENSE).
