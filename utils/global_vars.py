from utils.model_select import model_select
import os 
from glob import glob

MODEL_USE = 'maskrcnn'
MODEL_PATH, WEIGHTS_PATH = model_select(MODEL_USE)
IMAGE_PATH = 'raw_data/' 
MAIN_PATH = 'airport_dataset/runway/'
TEST_IMAGE_PATH = os.path.join(MAIN_PATH, IMAGE_PATH)
test_img = glob(f'{TEST_IMAGE_PATH}/*.png')
data_set_prefix = 'runway'
