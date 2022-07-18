from detectron2.config import get_cfg
from detectron2 import model_zoo
import os
from utils.model_select import model_select

MODEL_PATH, WEIGHTS_PATH = model_select('maskrcnn')

def cfg_test():
    """_summary_

    Returns:
        _type_: _description_
    """    
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file(MODEL_PATH))
    cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR,  WEIGHTS_PATH)
    # Here you could specify a custom path to the saved model
    # cfg.MODEL.WEIGHTS = '../input/wheat-detection-retinanet-faster-rcnn-101/model_final.pth'
    cfg.MODEL.DEVICE = "cpu"
    cfg.DATASETS.TEST = ('runway',)
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1    
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.8
    return cfg