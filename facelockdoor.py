import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
import time
import pyttsx3

# Get the training data we previously made
data_path = './FACE/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

# Create arrays for training data and labels
Training_data, Lebels = [],[]

# Open training images in our datapath
# Create a numpy array for training data
for i , files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    Training_data.append(np.asarray(images,dtype = np.uint8)) 
    Lebels.append(i)

# Create a numpy array for both training data and labels
Lebels = np.asarray(Lebels, dtype = np.int32)

# Initialize facial recognizer
model = cv2.face.LBPHFaceRecognizer_create()

# Let's train our model 
model.train(np.asarray(Training_data),np.asarray(Lebels))
print("training complete")
# face_classifier = cv2.CascadeClassifier('C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')


