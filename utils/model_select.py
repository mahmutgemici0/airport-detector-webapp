def model_select(MODEL_USE):
    models = {
    'rpn_r50_fpn': {
        'model_path': 'COCO-Detection/rpn_R_50_FPN_1x.yaml',
        'weights_path': 'none'},
    'faster_rcnn_50': {
        'model_path': 'COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml',
        'weights_path': 'none'},
    'faster_rcnn_101': {
        'model_path': 'COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml',
        'weights_path': 'none'},
    'maskrcnn': {
        'model_path': 'COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml',
        'weights_path': 'model_0009999.pth'}}

    if MODEL_USE == 'maskrcnn':
        return models[MODEL_USE]['model_path'], models[MODEL_USE]['weights_path']

