import cv2
import os
import pickle
from PIL import Image
import numpy as np

def train():
    cascade = cv2.CascadeClassifier ("haarcascade_frontalface default.xml")
    rainer e = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_id = {} # dictionary
    face_train = [] # list
    face_label = [] # list

    # Finding the path of the base directory
    BASE_DIR = os.path.dirname(os.path.abspath(_file_))
    my_face_dir = os.path.join(BASE_DIR, ‘dataset’)

    for root,  rain, files in os.walk(my_face_dir):
        for file in files:
            if file.endswith(“png”) or file.endswith(“jpg”):
                path = os.path.join(root, file)
                label = os.path.basename(root).lower()

                if not label in label_id:
                    label_id[label] = current_id
                    current_id += 1
                ID = label_id[label]

                pil_image = Image.open(path).convert(“L”)
                image_array = np.array(pil_image, “uint8”)

                face = cascade.detectMultiScale(image_array)

                for x, y, w, h in face:
                    img = image_array[y:y+h, x:x+w]
                    face_train.append(img)
                    face_label.append(ID)

    with open(“labels.pickle”, ‘wb’) as f:
        pickle.dump(label_id, f)

     rainer e.train(face_train, np.array(face_label))
     rainer e.save(“ rainer.yml”)
