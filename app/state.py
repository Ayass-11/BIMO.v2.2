from enum import Enum

class BIMOState(Enum):
    IDLE = "idle"
    PASSIVE_LISTENING = "passive_listening"
    WAKE_DETECTED = "wake_detected"
    ACTIVE_LISTENING = "active_listening"
    TRANSCRIBING = "transcribing"
    THINKING = "thinking"
    SPEAKING = "speaking"
    COOLDOWN = "cooldown"
    ERROR = "error"

