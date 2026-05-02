import os
import numpy as np
import wave
from openwakeword.train import train

POSITIVE_DIR = "data/wakeword/positive"
NEGATIVE_DIR = "data/wakeword/negative"
OUTPUT_DIR = "data/wakeword/model"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_wav(path):
    with wave.open(path, 'r') as f:
        frames = f.readframes(f.getnframes())
        audio = np.frombuffer(frames, dtype=np.int16)
        return audio.astype(np.float32) / 32768.0

def main():
    print("=== Hey BIMO - Model Eğitimi ===")

    positive_files = [
        os.path.join(POSITIVE_DIR, f)
        for f in os.listdir(POSITIVE_DIR)
        if f.endswith(".wav")
    ]
    negative_files = [
        os.path.join(NEGATIVE_DIR, f)
        for f in os.listdir(NEGATIVE_DIR)
        if f.endswith(".wav")
    ]

    print(f"Pozitif: {len(positive_files)} kayıt")
    print(f"Negatif: {len(negative_files)} kayıt")

    train(
        model_name="hey_bimo",
        positive_reference_clips=positive_files,
        negative_reference_clips=negative_files,
        output_dir=OUTPUT_DIR
    )

    print(f"\nModel kaydedildi: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
