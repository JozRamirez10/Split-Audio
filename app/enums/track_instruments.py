from enum import Enum;

class TrackInstruments(str, Enum):
    DRUMS = "drums"
    BASS = "bass"
    OTHER = "other"
    PIANO = "piano"
    GUITAR = "guitar"
    VOCALS = "vocals"