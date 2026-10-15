from enum import Enum

class GuitarRoleInstruments(str, Enum):
    RYTHM = "rythm_guitar"
    LEAD = "lead_guitar"

class GuitarTypeInstruments(str, Enum):
    ELECTRIC = "electric_guitar"
    ACOUSTIC = "acoustic_guitar"