import sounddevice as sd
import numpy as np
import time
from app.controller import Controller
from app.stt import STT
from app.llm import LLM
from app.tts import TTS
from app.input_handler import is_speech
from config.settings import AUDIO_SAMPLE_RATE, AUDIO_CHANNELS, AUDIO_MIN_SECONDS, WAKE_WORD_COOLDOWN

def session_loop(wake_word_detector):
    print("[BIMO] Session started. Say 'Bye BIMO' to end.")

    controller = Controller(
        stt=STT(),
        llm=LLM(),
        tts=TTS()
    )

    while True:
        print("[BIMO] Listening in session... (speak or say 'Bye BIMO')")
        audio_chunks = []
        speech_started = False
        silence_count = 0
        bye_detected = False
        SILENCE_LIMIT = 25

        with sd.InputStream(samplerate=AUDIO_SAMPLE_RATE, channels=AUDIO_CHANNELS, dtype='int16') as stream:
            while True:
                chunk, _ = stream.read(1280)
                flat = chunk.flatten()

                if wake_word_detector.detect_bye(flat):
                    bye_detected = True
                    break

                audio_chunks.append(chunk)
                speaking = is_speech(flat)

                if not speech_started and speaking:
                    speech_started = True
                    silence_count = 0

                if speech_started:
                    if not speaking:
                        silence_count += 1
                    else:
                        silence_count = 0
                    if silence_count >= SILENCE_LIMIT:
                        break

        if bye_detected:
            print("[BIMO] Bye BIMO detected. Session ending.")
            controller.tts.speak("See you later!")
            break

        if not speech_started or not audio_chunks:
            continue

        audio = np.concatenate(audio_chunks, axis=0)
        if len(audio) < AUDIO_SAMPLE_RATE * AUDIO_MIN_SECONDS:
            continue

        print("[BIMO] Processing...")
        controller.run_once(audio)
        time.sleep(WAKE_WORD_COOLDOWN)
        wake_word_detector.reset()
