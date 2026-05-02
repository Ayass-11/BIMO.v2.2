import sounddevice as sd
import numpy as np
import webrtcvad
from pynput import keyboard as kb
from config.settings import AUDIO_SAMPLE_RATE, AUDIO_CHANNELS, AUDIO_MIN_SECONDS

vad = webrtcvad.Vad(1)

def is_speech(flat):
    try:
        return vad.is_speech(flat[:320].tobytes(), AUDIO_SAMPLE_RATE)
    except:
        return False

def record_manual():
    print("[BIMO] Manual - hold SPACE and speak...")
    audio_chunks = []
    done = False

    def on_release(key):
        nonlocal done
        if key == kb.Key.space:
            done = True
            return False

    with kb.Listener(on_release=on_release) as listener:
        with sd.InputStream(samplerate=AUDIO_SAMPLE_RATE, channels=AUDIO_CHANNELS, dtype='int16') as stream:
            while not done:
                chunk, _ = stream.read(1280)
                audio_chunks.append(chunk)
        listener.join()

    if not audio_chunks:
        return None

    audio = np.concatenate(audio_chunks, axis=0)
    if len(audio) < AUDIO_SAMPLE_RATE * AUDIO_MIN_SECONDS:
        print("[BIMO] Too short.")
        return None

    print("[BIMO] Processing...")
    return audio

def listen_for_trigger(wake_word_detector):
    print("[BIMO] Listening... (say 'Hey BIMO' or hold SPACE)")

    space_pressed = False
    triggered = [None]

    def on_press(key):
        nonlocal space_pressed
        if key == kb.Key.space and not space_pressed:
            space_pressed = True
            triggered[0] = "manual"

    listener = kb.Listener(on_press=on_press)
    listener.start()

    with sd.InputStream(samplerate=AUDIO_SAMPLE_RATE, channels=AUDIO_CHANNELS, dtype='int16') as stream:
        while triggered[0] is None:
            chunk, _ = stream.read(1280)
            flat = chunk.flatten()
            if wake_word_detector.process(flat):
                triggered[0] = "wake"

    listener.stop()
    return triggered[0]
