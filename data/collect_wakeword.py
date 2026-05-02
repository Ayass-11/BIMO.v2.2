import sounddevice as sd
import numpy as np
import wave
import os
from pynput import keyboard as kb

SAMPLE_RATE = 16000
CHANNELS = 1
OUTPUT_DIR = "data/wakeword/positive"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def record_sample(index):
    print(f"\n[{index}] Hazır olunca SPACE'e bas, 'Hey BIMO' de, bırak.")
    audio_chunks = []
    recording = False
    done = False

    def on_press(key):
        nonlocal recording
        if key == kb.Key.space and not recording:
            recording = True
            print("   Kayıt başladı...")

    def on_release(key):
        nonlocal done
        if key == kb.Key.space:
            done = True
            return False

    with kb.Listener(on_press=on_press, on_release=on_release) as listener:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16') as stream:
            while not done:
                chunk, _ = stream.read(1024)
                if recording:
                    audio_chunks.append(chunk)
        listener.join()

    if not audio_chunks:
        return False

    audio = np.concatenate(audio_chunks, axis=0)
    path = os.path.join(OUTPUT_DIR, f"hey_bimo_{index:03d}.wav")

    with wave.open(path, 'w') as f:
        f.setnchannels(CHANNELS)
        f.setsampwidth(2)
        f.setframerate(SAMPLE_RATE)
        f.writeframes(audio.tobytes())

    print(f"   Kaydedildi: {path}")
    return True

def main():
    print("=== Hey BIMO - Ses Kaydı Toplama ===")
    print("Her seferinde farklı ton ve hızda söyle.")
    print("Çıkmak için Ctrl+C\n")

    index = 1
    while True:
        try:
            record_sample(index)
            index += 1
        except KeyboardInterrupt:
            print(f"\nToplam {index-1} kayıt tamamlandı.")
            break

if __name__ == "__main__":
    main()
