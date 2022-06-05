from dataclasses import dataclass, field
from deepface import DeepFace
import cv2
import numpy as np

@dataclass
class FaceEmotionRecognition:
    _face_cascade: None = field(init=False)
    
    def __post_init__(self) -> None:
        self._face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
    def detect_emotion(self, image):
        face = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_UNCHANGED)
        copy_img = face

        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            
        faces = self._face_cascade.detectMultiScale(gray, 1.1, 7)
        for (x, y, w, h) in faces:
            try:
                cv2.rectangle(copy_img, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 3)
                font = cv2.FONT_HERSHEY_SIMPLEX
                crop_img = copy_img[y:y+h, x:x+w]
                emotion = DeepFace.analyze(crop_img, actions=['emotion'],enforce_detection=False)
                cv2.putText(copy_img, emotion['dominant_emotion'], (x-40,y-40), font, 2, (17,255,0), 2,cv2.LINE_AA)
            except:
                pass

        return copy_img
