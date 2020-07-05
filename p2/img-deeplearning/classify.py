# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
 
class Classify:
    model = None
    mlb = None
    def __init__(self,model,labelbin):
        self.model = load_model(model)
        self.mlb = pickle.loads(open(labelbin, "rb").read())

    def specify(self,image):
        image = cv2.resize(image, (96, 96))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        #image = imutils.resize(image, width=400)
        print("[INFO] classifying image...")
        proba = self.model.predict(image)[0]
        idxs = np.argsort(proba)[::-1][:2]
        #print(self.mlb.classes_[max(idxs)])

        # loop over the indexes of the high confidence class labels
        for (i, j) in enumerate(idxs):
            # build the label and draw the label on the image
            label = "{}: {:.2f}%".format(self.mlb.classes_[j], proba[j] * 100)
            cv2.putText(image, label, (10, (i * 30) + 25), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # show the probabilities for each of the individual labels
        for (label, p) in zip(self.mlb.classes_, proba):
            print("{}: {:.2f}%".format(label, p * 100))
        
        ii = [i for i, j in enumerate(proba) if j == max(proba)]
        
        return "{} : {:.2f}%".format(self.mlb.classes_[ii][0],max(proba)*100)
        #ii = [i for i, j in enumerate(idxs) if j == max(idxs)]
       
        

        