import sounddevice as sd
from kokoro import KPipeline
from config.settings import TTS_LANG, TTS_VOICE, TTS_SPEED, TTS_SAMPLE_RATE

class TTS:
    def __init__(self):
        print("[TTS] Loading Kokoro pipeline...")
        self.pipeline = KPipeline(lang_code=TTS_LANG)
        self.voice = TTS_VOICE
        self.speed = TTS_SPEED
        self.is_speaking = False
        print("[TTS] Ready.")

    def speak(self, text: str):
        try:
            self.is_speaking = True
            generator = self.pipeline(text, voice=self.voice, speed=self.speed)
            for _, _, audio in generator:
                sd.play(audio, samplerate=TTS_SAMPLE_RATE)
                sd.wait()
        except Exception as e:
            print(f"[TTS] Error: {e}")
        finally:
            self.is_speaking = False
