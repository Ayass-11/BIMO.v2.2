from faster_whisper import WhisperModel
import numpy as np
from config.settings import STT_MODEL_SIZE, STT_DEVICE, STT_COMPUTE_TYPE, STT_LANGUAGE

class STT:
    def __init__(self):
        print("[STT] Loading Whisper model...")
        self.model = WhisperModel(STT_MODEL_SIZE, device=STT_DEVICE, compute_type=STT_COMPUTE_TYPE)
        print("[STT] Model ready.")

    def transcribe(self, audio: np.ndarray) -> str:
        audio_float = audio.astype(np.float32) / 32768.0
        audio_flat = audio_float.flatten()

        segments, _ = self.model.transcribe(audio_flat, language=STT_LANGUAGE)
        text = " ".join([segment.text for segment in segments]).strip()

        return text if text else ""
