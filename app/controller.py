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
                text = self.stt.transcribe(audio_input)
                print(f"[STT] '{text}'")
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
                response = self.llm.respond(text)
                print(f"[LLM] '{response}'")
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
                self.tts.speak(response)
            except Exception as e:
                print(f"[ERROR][TTS] {e}")
                self.set_state(BIMOState.IDLE)
                return

            self.set_state(BIMOState.IDLE)

        except Exception as e:
            self.set_state(BIMOState.ERROR)
            print(f"[ERROR][UNKNOWN] {e}")
            self.state = BIMOState.IDLE
