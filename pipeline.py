import config
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import pathlib
import numpy as np
from PIL import ImageDraw


def to_str(i):
    if i == 0:
        return 'blocked'
    elif i == 1:
        return 'clear'
    elif i == 2:
        return 'partial'
    else:
        raise Exception('Invalid integer')


print('[MODELS] Loading models...')
object_localizer_model = load_model(pathlib.Path.cwd() / 'saved_models' / 'object_localizer_models' / config.object_localizer_model_name)
image_classifier_model = load_model(pathlib.Path.cwd() / 'saved_models' / 'image_classifier_models' / config.image_classifier_model_name)
print('[MODELS] Models loaded.')

imgpath = input('Path of image: ')

print('[OBJECT LOCALIZER] Predicting bounding box...')
img = load_img(imgpath, target_size=config.object_localizer_image_size)
img_arr = img_to_array(img)
img_arr = np.expand_dims(img_arr, axis=0)
pred = object_localizer_model.predict(img_arr)
bbox = pred[0]
bbox *= config.object_localizer_image_size[0]
img_copy = img.copy()
draw = ImageDraw.Draw(img_copy)
draw.rectangle(bbox, outline='red', width=1)
img_copy.show()
print(f'[OBJECT LOCALIZER] Prediction: {bbox}')


print('[IMAGE CLASSIFIER] Predicting classification...')
bboximg = img.crop(tuple(bbox)).resize(config.image_classifier_image_size)
img_arr = img_to_array(bboximg)
img_arr = np.expand_dims(img_arr, axis=0)
pred = image_classifier_model.predict(img_arr)
pred_str = to_str(np.argmax(pred[0]))
print(f'[IMAGE CLASSIFIER] Prediction: {pred[0]} ({pred_str})')
