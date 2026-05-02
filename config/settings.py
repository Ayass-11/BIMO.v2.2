# Model
LLM_MODEL = "llama3.1:8b"
LLM_HOST = "http://localhost:11434"
LLM_MAX_HISTORY = 20

# STT
STT_MODEL_SIZE = "base"
STT_DEVICE = "cpu"
STT_COMPUTE_TYPE = "int8"
STT_LANGUAGE = "en"

# TTS
TTS_VOICE = "am_michael"
TTS_SPEED = 1.1
TTS_LANG = "a"
TTS_SAMPLE_RATE = 24000

# Audio
AUDIO_SAMPLE_RATE = 16000
AUDIO_CHANNELS = 1
AUDIO_MIN_SECONDS = 0.5

# Wake Word
WAKE_WORD_MODEL = "models/wakeword/hey_bee_mo.onnx"
WAKE_WORD_THRESHOLD = 0.8
WAKE_WORD_COOLDOWN = 3.0

BYE_WORD_MODEL = "models/wakeword/bye_bee_mo.onnx"
BYE_WORD_THRESHOLD = 0.8
