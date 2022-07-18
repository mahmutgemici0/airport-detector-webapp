from turtle import width
import streamlit as st
import random 
from detectron2.data import datasets, DatasetCatalog, MetadataCatalog, build_detection_train_loader, build_detection_test_loader
from utils.create_subdf import *
from utils.dataset import *
from utils.register_dataset import *
from utils.cfg_test import *
from utils.model_select import *
from utils.visual_predict import *
from utils.global_vars import *
import lib.satellite_imagery as sat
import sys

st.title('Airport Detection on Satellite Imagery')
# st.text('Contributors: Mahmut Gemici, Dr. Nidhal C. Bouaynaya, Cliff Johnson')

lat = st.sidebar.number_input("Latitude", value=40.853894)
lon = st.sidebar.number_input("Longitude", value=-74.060218)
zoom = st.sidebar.number_input("Zoom", value=15)

#Display the coordinate on map
df = pd.DataFrame({"lat": [lat], "lon": [lon], "zoom": [zoom]})
st.map(df)

#Download the satellite image
file_name = "airport_dataset/runway/raw_data/{}_{:04d}.png".format('test', 1)
image = sat.grab_image(lat, lon, zoom, file_name)
#Display the satellite image
img = cv2.imread(file_name)
st.title(f'Satellite View at ({lat},{lon})')
display_image = st.image(img, width= 700)
st.title('Inferred Image;')

def main():
    sub_df = create_subdf(test_img)
    DatasetCatalog.clear() 
    register_dataset(data_set_prefix = 'runway', IMAGE_PATH = 'raw_data/')
    cfg = cfg_test()
    predictor = DefaultPredictor(cfg)   
    visual_predict(test_img)             

if __name__ == "__main__":
    main()

