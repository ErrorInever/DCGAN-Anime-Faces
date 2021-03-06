from easydict import EasyDict as edict

__C = edict()

cfg = __C
# Other
__C.PROJECT_NAME = "DCGAN-Anime-Faces"
__C.PROJECT_VERSION_NAME = "Default-DCGAN"
# Global
__C.NUM_EPOCHS = 50
__C.LEARNING_RATE = 0.0002
__C.BATCH_SIZE = 128
__C.DATASET_SIZE = None
# CHANNELS
__C.IMG_SIZE = 64
__C.CHANNELS_IMG = 3
__C.Z_DIMENSION = 128
# Models
__C.FEATURES_DISC = 64
__C.FEATURES_GEN = 64
# Paths and saves
__C.SAVE_EACH_EPOCH = 25
__C.OUT_DIR = ""
__C.SAVE_CHECKPOINT_PATH = ""

# Display results
__C.NUM_SAMPLES = 64    # size grid for display images
__C.FREQ = 50
