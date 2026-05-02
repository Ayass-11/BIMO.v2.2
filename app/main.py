import time
from app.wake_word import WakeWord
from app.input_handler import listen_for_trigger, record_manual
from app.session import session_loop
from app.controller import Controller
from app.stt import STT
from app.llm import LLM
from app.tts import TTS
from config.settings import WAKE_WORD_COOLDOWN

def main():
    wake_word_detector = WakeWord()

    print("[BIMO] v2.1 started. Say 'Hey BIMO' or hold SPACE to talk.")
    while True:
        trigger = listen_for_trigger(wake_word_detector)

        if trigger == "manual":
            controller = Controller(
                stt=STT(),
                llm=LLM(),
                tts=TTS()
            )
            audio = record_manual()
            if audio is not None:
                controller.run_once(audio)
                print("[BIMO] Cooling down...")
                time.sleep(WAKE_WORD_COOLDOWN)
                wake_word_detector.reset()
        else:
            time.sleep(0.6)
            session_loop(wake_word_detector)

if __name__ == "__main__":
    main()

