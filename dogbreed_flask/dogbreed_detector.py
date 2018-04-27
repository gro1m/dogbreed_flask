import os
import tensorflow as tf
from keras.preprocessing import image
from flask import Flask, request, render_template, send_from_directory
from keras.models import load_model
from keras.applications.resnet50 import preprocess_input, decode_predictions, ResNet50
import cv2
import numpy as np

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

from extract_bottleneck_features import *
dognames_txt = open("dognames.txt","r")
dog_names     = dognames_txt.read().split('\n')
Xception_model = load_model('saved_models/Xception.best_weights.hdf5')

# define ResNet50 model
ResNet50_model = ResNet50(weights='imagenet')

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def Xception_predictbreed(img_path):
    Xception_bottlenecks = extract_Xception(path_to_tensor(img_path))
    Xception_prediction  = Xception_model.predict(Xception_bottlenecks)
    return dog_names[np.argmax(Xception_prediction)]

def ResNet50_predict_labels(img_path):
    # returns prediction vector for image located at img_path
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

### returns "True" if a dog is detected in the image stored at img_path
def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151)) 

# extract pre-trained face detector
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

def face_detector(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0

def Xception_detector(img_path):
    fd = face_detector(img_path)         #detect human face
    dd = dog_detector(img_path)          #detect dog
    pd = Xception_predictbreed(img_path) #predicted breed

    if(fd==True and dd==False):
        s1 = "You are human, and the dog breed you resemble most is "
    elif(fd==False and dd==True):
        if(pd[0]=="A" or pd[0]=="E" or pd[0]=="I" or pd[0]=="O" or pd[0]=="U"):
            s1 = "You are an "
        else:
            s1 = "You are a "           
    else:
        s1 = "Well, the dog breed you resemble most is "
    return s1 + pd

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Upload directory: {}".format(target), "already exists")
    filename = ""
    destination = ""
    detection = " "
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Save image file to:", destination)
        upload.save(destination)
        detection = Xception_detector(destination)
    return render_template("complete.html", image_name=filename, text_str = detection)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)
