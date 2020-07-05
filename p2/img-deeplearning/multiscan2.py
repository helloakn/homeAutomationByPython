'''
multi classificatio / multi face detection / multi face recognization
'''
# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

#================================ Start Class ================================#
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
        # show the probabilities for each of the individual labels
        for (label, p) in zip(self.mlb.classes_, proba):
            print("{}: {:.2f}%".format(label, p * 100))
        
        ii = [i for i, j in enumerate(proba) if j == max(proba)]
        
        return "{} : {:.2f}%".format(self.mlb.classes_[ii][0],max(proba)*100)
        #ii = [i for i, j in enumerate(idxs) if j == max(idxs)]
          
#================================ End Class ================================#



model = "model/face_lady_man.model"
labelbin = "model/labelbin/face_lady_man"

_classify = Classify(model,labelbin)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('FaceRecognize/trainer/trainer.yml')
cascadePath = "FaceRecognize/Cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
#----FONT
'''
CV_FONT_HERSHEY_SIMPLEX normal size sans-serif font
CV_FONT_HERSHEY_PLAIN small size sans-serif font
CV_FONT_HERSHEY_DUPLEX normal size sans-serif font (more complex than CV_FONT_HERSHEY_SIMPLEX )
CV_FONT_HERSHEY_COMPLEX normal size serif font
CV_FONT_HERSHEY_TRIPLEX normal size serif font (more complex than CV_FONT_HERSHEY_COMPLEX )
CV_FONT_HERSHEY_COMPLEX_SMALL smaller version of CV_FONT_HERSHEY_COMPLEX
CV_FONT_HERSHEY_SCRIPT_SIMPLEX hand-writing style font
CV_FONT_HERSHEY_SCRIPT_COMPLEX more complex variant of CV_FONT_HERSHEY_SCRIPT_SIMPLEX
'''
font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['0', 
'AKN','ManGate','yu may khin'
] 
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
xx = 0
while True:
    xx = xx +1
    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        print(confidence)
        # Check if confidence is less them 100 ==> "0" is perfect match 
        print(id)
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        print(id)
        #--------------
        #crop and classify
        text = _classify.specify(img[y:y+h, x:x+w])
        #print(text)
        #--------------
        
        cv2.putText(img, str(text), (x+5,y-5), font, 1,(255,255,255), 2)
        cv2.putText(img, str(id), (x+5,y+20), font, 1,(255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (165,88,88), 1)  
    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()