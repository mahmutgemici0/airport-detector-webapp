import cv2
import os
from glob import glob
import streamlit as st
from utils.cfg_test import cfg_test
from detectron2.engine import DefaultPredictor, DefaultTrainer
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.data import datasets, DatasetCatalog, MetadataCatalog, build_detection_train_loader, build_detection_test_loader

from utils.global_vars import *

cfg = cfg_test()
predictor = DefaultPredictor(cfg)
micro_metadata = MetadataCatalog.get(f"{data_set_prefix}_{IMAGE_PATH[:-1]}")

def visual_predict(dataset):  
    for sample in test_img:
        st.write(f'Processing image: {sample}')
        img = cv2.imread(sample)
        output = predictor(img)
        
        v = Visualizer(img[:, :, ::-1], metadata=micro_metadata, scale=1)
        v = v.draw_instance_predictions(output['instances'].to('cpu'))
        outputs = st.image(v.get_image()[:, :, ::-1], cv2.COLOR_BGRA2BGR, width = 700)    
    return outputs
