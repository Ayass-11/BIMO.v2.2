[README.md](https://github.com/user-attachments/files/34149102/README.md)

# BIMO.v2.2

**BIMO** is a locally running, voice-based AI companion built with Python. It combines speech recognition, a local language model, and speech synthesis to support spoken conversations without cloud inference.

BIMO is a personal project focused on building a modular voice interaction system. After the required models have been downloaded, its conversation pipeline can run locally without an internet connection.

## Features

- **Wake-word activation:** Say **"Hey BIMO"** to start a hands-free conversation session.
- **Voice-controlled session ending:** Say **"Bye BIMO"** to end the active session.
- **Push-to-talk:** Hold **SPACE** to record a single manual request.
- **Speech and silence detection:** Uses WebRTC Voice Activity Detection (VAD) to detect speech and identify pauses.
- **Local speech-to-speech pipeline:** Transcribes speech, generates a response, and speaks it aloud.
- **Session-based conversation history:** Keeps recent messages in context during an active session (not saved across restarts).
- **Configurable behavior:** Model, language, voice, audio, and wake-word settings are managed in `config/settings.py`.

The current implementation is focused on **English** conversations.

## Tech stack

| Component | Technology | Purpose |
| --- | --- | --- |
| Programming language | Python | Application logic and orchestration |
| Speech-to-text | faster-whisper (Whisper) | Transcribes microphone input |
| Language model | Llama 3.1 8B via Ollama | Generates conversational responses locally |
| Text-to-speech | Kokoro TTS | Produces spoken responses |
| Wake-word detection | openWakeWord | Detects "Hey BIMO" and "Bye BIMO" |
| Voice activity detection | WebRTC VAD | Detects speech and silence |
| Audio and input | sounddevice, NumPy, pynput | Audio capture/playback and keyboard input |

## How it works

```text
Microphone
    |
    +--> "Hey BIMO" (wake word) --> Conversation session
    |                                  |
    |                             Speech detection (VAD)
    |                                  |
    +--> SPACE (push-to-talk) ---------+
                                       |
                              Whisper (speech-to-text)
                                       |
                              Ollama / Llama 3.1 8B
                                       |
                              Kokoro (text-to-speech)
                                       |
                                    Speaker
```

The application separates input handling, session management, speech recognition, language model interaction, and speech synthesis into individual modules.

## Getting started

### Requirements

- Linux environment (developed on Linux Mint)
- Python 3 and `venv`
- Working microphone and audio output
- [Ollama](https://ollama.com/) installed and running
- Internet access for the **initial** installation and model downloads

### 1. Clone the repository

```bash
git clone https://github.com/Ayass-11/BIMO.v2.2.git
cd BIMO.v2.2
```

### 2. Create a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Linux audio/speech dependencies

For Ubuntu/Linux Mint-based systems:

```bash
sudo apt install espeak-ng alsa-utils
```

Additional system audio packages may be required depending on your Linux installation.

### 5. Prepare the local language model

```bash
ollama pull llama3.1:8b
```

Make sure Ollama is running before starting BIMO. The wake-word models are expected at the paths configured in `config/settings.py` (under `models/wakeword/`). Other speech models may be downloaded automatically on first use.

### 6. Start BIMO

From the repository root:

```bash
python3 -m app.main
```

## Usage

| Action | How to use |
| --- | --- |
| Start a hands-free session | Say **"Hey BIMO"** |
| Speak during the session | Talk normally; speech/silence detection handles turns |
| End the session | Say **"Bye BIMO"** |
| Send one manual voice request | Hold **SPACE**, speak, and release |

## Project structure

```text
BIMO.v2.2/
├── app/
│   ├── main.py           # Entry point and trigger handling
│   ├── input_handler.py  # Microphone, keyboard and VAD input
│   ├── wake_word.py      # Wake-word models and detection
│   ├── session.py        # Hands-free conversation sessions
│   ├── controller.py     # STT -> LLM -> TTS orchestration
│   ├── stt.py            # Speech-to-text
│   ├── llm.py            # Local LLM and session history
│   ├── tts.py            # Speech synthesis
│   └── state.py          # Application states
├── config/
│   └── settings.py       # Centralized configuration
├── models/
│   └── wakeword/         # Wake-word model files
├── requirements.txt
└── README.md
```

*The tree highlights the main application files rather than every directory in the repository.*

## Current status and roadmap

**Available in the current code:** local voice conversation, wake-word activation, push-to-talk, voice activity detection, session ending by voice, and in-session conversation context.

**Planned / under development:** improved conversational flow, more flexible personality customization, and persistent memory across sessions. Multilingual support, vision, web access, and computer control are **not** part of the current working version.

BIMO is an evolving personal learning and development project, not a production-ready assistant.
