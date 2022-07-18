from detectron2.data import datasets, DatasetCatalog, MetadataCatalog, build_detection_train_loader, build_detection_test_loader

def register_dataset(data_set_prefix = 'runway', IMAGE_PATH = 'raw_data/'):
    for d in [IMAGE_PATH]:   
        DatasetCatalog.register(
            f"{data_set_prefix}_{d}",
            lambda d=d: runway_dataset(
                train_df if d == "train" else sub_df,
                TRAIN_IMAGE_PATH if d == "train" else TEST_IMAGE_PATH,
                True if d == "train" else False,
            ),
        )