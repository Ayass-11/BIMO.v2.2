
import time
from app.state import BIMOState


class Controller:
    def __init__(self, stt, llm, tts):
        self.stt = stt
        self.llm = llm
        self.tts = tts
        self.state = BIMOState.IDLE

    def set_state(self, new_state: BIMOState):
        print(f"[BIMO] State: {self.state.value} → {new_state.value}")
        self.state = new_state

    def run_once(self, audio_input):
        try:
            self.set_state(BIMOState.ACTIVE_LISTENING)

            self.set_state(BIMOState.TRANSCRIBING)
            try:
                t0 = time.perf_counter()
                text = self.stt.transcribe(audio_input)
                t1 = time.perf_counter()

                print(f"[STT] '{text}'")
                print(f"[TIMING] STT: {t1 - t0:.2f}s")

            except Exception as e:
                print(f"[ERROR][STT] {e}")
                self.set_state(BIMOState.IDLE)
                return

            if not text or not text.strip():
                print("[BIMO] No speech detected, returning to idle.")
                self.set_state(BIMOState.IDLE)
                return

            self.set_state(BIMOState.THINKING)
            try:
                t2 = time.perf_counter()
                response = self.llm.respond(text)
                t3 = time.perf_counter()

                print(f"[LLM] '{response}'")
                print(f"[TIMING] LLM: {t3 - t2:.2f}s")

            except Exception as e:
                print(f"[ERROR][LLM] {e}")
                self.set_state(BIMOState.IDLE)
                return

            if not response or not response.strip():
                print("[BIMO] Empty response from LLM, returning to idle.")
                self.set_state(BIMOState.IDLE)
                return

            self.set_state(BIMOState.SPEAKING)
            try:
                t4 = time.perf_counter()
                self.tts.speak(response)
                t5 = time.perf_counter()

                stt_time = t1 - t0
                llm_time = t3 - t2
                tts_time = t5 - t4
                total_time = t5 - t0

                print(f"[TIMING] TTS Total: {tts_time:.2f}s")
                print(f"[TIMING] STT + LLM: {stt_time + llm_time:.2f}s")
                print(f"[TIMING] Total elapsed: {total_time:.2f}s")

            except Exception as e:
                print(f"[ERROR][TTS] {e}")
                self.set_state(BIMOState.IDLE)
                return

            self.set_state(BIMOState.IDLE)

        except Exception as e:
            self.set_state(BIMOState.ERROR)
            print(f"[ERROR][UNKNOWN] {e}")
            self.state = BIMOState.IDLE

