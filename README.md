# BIMO.v1

BIMO is a locally running AI assistant that can be customized to personal preferences.

## What is BIMO.v1?

BIMO.v1 is the first working software core of the BIMO project.
It runs entirely on your local machine — no cloud, no internet dependency.

This version focuses on one thing: a stable, characterful voice conversation loop.

## What does v1 do?

- Takes voice input via push-to-talk (SPACE key)
- Converts speech to text using Whisper
- Sends text to a local language model via Ollama
- Converts the response back to speech using Kokoro TTS
- Repeats this loop continuously

## What does v1 NOT do?

- No wake word detection
- No persistent memory across sessions
- No computer control
- No camera or vision
- No web search
- No multi-language support (English only in v1)
- No companion mode

These are intentional scope decisions, not missing features.

## How to run

**1. Clone the project and navigate to the folder:**
```bash
cd BIMO.v1
```

**2. Create and activate virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Install system dependencies:**
```bash
sudo apt install espeak-ng alsa-utils
```

**5. Pull the language model via Ollama:**
```bash
ollama pull llama3.1:8b
```

**6. Run BIMO:**
```bash
python3 -m app.main
```

**7. Usage:**
- Hold SPACE to talk
- Release SPACE to send
- BIMO will respond with voice

## Dependencies

- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) — Speech to text
- [Ollama](https://ollama.com) — Local language model runtime
- [Kokoro TTS](https://github.com/hexgrad/kokoro) — Text to speech
- sounddevice, numpy, pynput — Audio and input handling

## Project structure

```
BIMO.v1/
├── app/
│   ├── main.py         # Entry point, push-to-talk loop
│   ├── controller.py   # Orchestrates the conversation chain
│   ├── stt.py          # Speech to text layer
│   ├── llm.py          # Language model layer
│   ├── tts.py          # Text to speech layer
│   └── state.py        # Application state definitions
├── config/
│   └── settings.py     # All configurable settings in one place
├── data/
├── docs/
├── logs/
├── tests/
├── requirements.txt
└── .gitignore
```

## Configuration

All settings are in `config/settings.py`.
You can change the model, voice, language, speed, and audio settings from there without touching the code.

## Why English only in v1?

English was chosen as the first language to keep v1 scope controlled and stable.
Turkish and multilingual support are planned for later versions.

## Status

BIMO.v1 — core complete. Voice conversation chain is stable and running.
