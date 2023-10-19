import tensorflow as tf
import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
import pickle

DIRECTORY = r'C:\Users\Entwan\Downloads\archive\dogscats\valid'
CATEGORIES = ['cats', 'dogs']

for category in CATEGORIES:
    folder = os.path.join(DIRECTORY,category)
    for img in os.listdir(folder):
        img_path = os.path.join(folder, img)
        img_arr = cv2.imread(img_path)
        plt.imshow(img_arr)
        break

