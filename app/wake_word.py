import numpy as np
from openwakeword.model import Model
from config.settings import WAKE_WORD_MODEL, WAKE_WORD_THRESHOLD, BYE_WORD_MODEL, BYE_WORD_THRESHOLD

class WakeWord:
    def __init__(self):
        print("[WakeWord] Loading models...")
        self.wake_model = Model(wakeword_model_paths=[WAKE_WORD_MODEL])
        self.bye_model = Model(wakeword_model_paths=[BYE_WORD_MODEL])
        self.wake_threshold = WAKE_WORD_THRESHOLD
        self.bye_threshold = BYE_WORD_THRESHOLD
        print("[WakeWord] Ready.")

    def process(self, audio_chunk: np.ndarray) -> bool:
        prediction = self.wake_model.predict(audio_chunk)
        for model_name, score in prediction.items():
            if score >= self.wake_threshold:
                print(f"[WakeWord] Hey BIMO detected! Score: {score:.2f}")
                return True
        return False

    def detect_bye(self, audio_chunk: np.ndarray) -> bool:
        prediction = self.bye_model.predict(audio_chunk)
        for model_name, score in prediction.items():
            if score >= self.bye_threshold:
                print(f"[WakeWord] Bye BIMO detected! Score: {score:.2f}")
                return True
        return False

    def reset(self):
        self.wake_model.reset()
        self.bye_model.reset()
