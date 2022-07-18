from tqdm.notebook import tqdm
import os 
import cv2

def runway_dataset(df, folder, is_train):
    """_summary_

    Args:
        df (dataframe) : sub_df --> submission dataframe
        folder (path string): TEST_IMAGE_PATH 
        is_train (bool): False --> because it's not training

    Returns:
        Dictionary: dataset dictionary
    """    
    unique_img_names = df["image_id"].unique().tolist()  # Take unique image names
    df_group = df.groupby("image_id")  # Group the training by the image ids
    dataset_dicts = []

    for img_id, img_name in enumerate(tqdm(unique_img_names)):
        img_group = df_group.get_group(img_name)  # Take all annotations for an image
        img_path = os.path.join(folder, img_name + ".png")  # Create path for an image
        if (
            is_train
        ):  # Using training set, where we have multiple bounding boxes per image

            record = dict()  # Create a record dictionary

            # Add image properties to the record
            record["file_name"] = img_path
            record["image_id"] = img_id
            record["height"] = int(img_group["height"].values[0])
            record["width"] = int(img_group["width"].values[0])

            annots = []  # Create annotation list
            for _, ant in img_group.iterrows():
                # bounding box is a string, so remove square brackets
                box = ant.bbox[1:-1]
                # Split the bbox values and convert it to float
                box = list(map(float, box.split(", ")))
                # Convert to int
                x, y, w, h = list(map(int, box))

                # Create annotation dictionary
                annot = {
                    "bbox": (
                        x,
                        y,
                        x + w,
                        y + h,
                    ),  # change to XYXY format. Original was in XYWH
                    "bbox_mode": BoxMode.XYXY_ABS,
                    "category_id": 0,  # only one category is present in this dataset
                }

                # Append each annotation to the list of annotation
                annots.append(dict(annot))

            record["annotations"] = list(annots)

        else:  # Using submission file, where each line is an image

            img = cv2.imread(img_path)
            h, w = img.shape[:2]

            record = dict()
            record["file_name"] = img_path
            record["image_id"] = img_id
            record["height"] = int(h)
            record["width"] = int(w)

        dataset_dicts.append(record)

    return dataset_dicts