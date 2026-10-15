from enum import Enum

class DrumInstruments(str, Enum):
    KICK = "kick"
    SNARE = "snare"
    TOMS = "toms"
    RIDE = "ride"
    CRASH = "crash"
    HI_HATS = "hh"