FORMAT_LOG = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
MAX_FILE_SIZE_MB = 200
ALLOWED_AUDIO_EXTENSIONS = [".wav", ".mp3", ".flac", ".m4a", ".ogg"]

# ----- Name services -----
TRACK_NAME = "Split Audio Service"
DRUMS_NAME = "Split Drums Service"
VOCAL_NAME = "Split Vocal Service"
WINDS_NAME = "Split Winds Service"
GUITAR_ROLE_NAME = "Split Guitar Role Service"
GUITAR_TYPE_NAME = "Split Guitar Type Service"

# ----- Models -----
TRACK_MODEL = "htdemucs_6s.yaml"
DRUMS_MODEL = "MDX23C-DrumSep-aufr33-jarredou.ckpt"
VOCAL_MODEL = "mel_band_roformer_karaoke_aufr33_viperx_sdr_10.1956.ckpt"
WINDS_MODEL = "17_HP-Wind_Inst-UVR.pth"
GUITAR_ROLE_WORKFLOW = "guitarrythm_guitarlead"
GUITAR_TYPE_WORKFLOW = "guitar_acoustic_electric"