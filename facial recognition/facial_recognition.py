# Import standard dependencies
import cv2
import os
import random
import numpy as np

# Import tensorflow dependencies - Functional API
from matplotlib import pyplot as plt
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Conv2D, Dense, MaxPooling2D, Input, Flatten
import tensorflow as tf

# Avoid OOM errors by setting GPU Memory Consumption Growth
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus: 
    tf.config.experimental.set_memory_growth(gpu, True)

# Setup paths
POS_PATH = os.path.join('data', 'positive') #the examples that are the same with our anchor image
NEG_PATH = os.path.join('data', 'negative') #the examples that are not the same with our anchor image
ANC_PATH = os.path.join('data', 'anchor') #the image we want to verify

# Make the directories
os.makedirs(POS_PATH)
os.makedirs(NEG_PATH)
os.makedirs(ANC_PATH)

