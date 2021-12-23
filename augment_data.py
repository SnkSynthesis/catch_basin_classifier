from keras.preprocessing.image import ImageDataGenerator, array_to_img
from glob import glob
from PIL import Image
import matplotlib.pyplot as plt
import os
import shutil
import numpy as np

widths = []
heights = []

for path in glob('data/**/**/*.JPG'):
    with Image.open(path) as img:
        widths.append(img.width)
        heights.append(img.height)

image_size = round(sum(widths) / len(widths)), round(sum(heights) / len(heights))

datagen = ImageDataGenerator(
    rescale=1/255.0,
    shear_range=0.2,
    brightness_range=[0.5, 1.2],
    rotation_range=30,
    zoom_range=0.4,
    horizontal_flip=True
)

generator = datagen.flow_from_directory(
    'data/training',
    classes=['blocked', 'clear', 'partial'],
    batch_size=32,
    class_mode='categorical',
    target_size=image_size
)

def classnum_to_classname(classnum):
    if classnum == 0:
        return 'blocked'
    elif classnum == 1:
        return 'clear'
    elif classnum == 2:
        return 'partial'
    else:
        raise Exception('Invalid argument')


shutil.rmtree('augmented_data/blocked')
shutil.rmtree('augmented_data/clear')
shutil.rmtree('augmented_data/partial')

os.mkdir('augmented_data/blocked')
os.mkdir('augmented_data/clear')
os.mkdir('augmented_data/partial')

batch = next(generator)
for i in range(10):
    for i, img in enumerate(batch[0]):
        classname = classnum_to_classname(np.argmax(batch[1][i]))
        images = os.listdir(f'augmented_data/{classname}')
        try:
            images.remove('.ipynb_checkpoints')
        except:
            pass
        image = array_to_img(batch[0][0])
        base_path = f'augmented_data/{classname}'
        if len(images) == 0:
            image.save(f'{base_path}/{classname[0].upper()}1.JPG')
        else:
            nums = list(map(lambda imgname: int(imgname.split('.')[0][1:]), images))
            nextnum = max(nums) + 1
            image.save(f'{base_path}/{classname[0].upper()}{nextnum}.JPG')
    batch = next(generator)
