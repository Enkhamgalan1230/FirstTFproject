import tensorflow as tf
# numpy is for array operations
import numpy as np
# cv2 is for converting images to array
import cv2
# os is for specify locations of images
import os
import random
# matplot helps with visualising
import matplotlib.pyplot as plt
# pickle is used for converting objects byte stream to store in database
import pickle
#
DIRECTORY = r'C:\Users\Entwan\Downloads\archive\dogscats\train'
CATEGORIES = ['cats', 'dogs']

IMG_SIZE = 50

for category in CATEGORIES:

    folder = os.path.join(DIRECTORY, category)
    for img in os.listdir(folder):
        img_path = os.path.join(folder, img)
        img_arr = cv2.imread(img_path)
        cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
        plt.imshow(img_arr)
        break
