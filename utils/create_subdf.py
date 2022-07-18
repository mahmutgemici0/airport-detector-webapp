import os
from glob import glob
import pandas as pd

def create_subdf(dataset):
    """
    This function creates a submission dataframe

    Args:
        dataset (list):  test_img --> contains list of image path

    Returns:
        dataframe: contains two columns.
        - imageid : id of the test images
        - PredictionString : preds
    """
    image_id = []
    predictionString = []
    for i in dataset:
        head, tail = os.path.split(i)
        id = tail.split('.')[0]    
        image_id.append(id)
        predictionString.append('')
    sub_df = pd.DataFrame({'image_id': image_id, 'PredictionString': predictionString})
    
    return sub_df