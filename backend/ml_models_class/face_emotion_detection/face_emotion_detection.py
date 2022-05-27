from dataclasses import dataclass, field
from deepface import DeepFace
import cv2

@dataclass
class FaceEmotionRecognition:
    _face_cascade: None = field(init=False)
    
    def __post_init__(self) -> None:
        self._face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
    def detect_emotion(self, image):
        face = cv2.imread(image)
        
        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            
        faces = self._face_cascade.detectMultiScale(gray, 1.1, 3)
        for (x, y, w, h) in faces:
            try:
                cv2.rectangle(image, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                crop_img = image[y:y+h, x:x+w]
                emotion = DeepFace.analyze(crop_img, actions=['emotion'],enforce_detection=False)
                cv2.putText(image, emotion['dominant_emotion'], (x-40,y-40), font, 1, (200,255,155))
            except:
                pass

        print(image)
        return image
