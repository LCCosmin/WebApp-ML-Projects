from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn.utils import resample
from ml_models_class.face_emotion_detection.face_emotion_detection import FaceEmotionRecognition
from ml_models_class.military_detection.military_detection import MilitaryDetector
import cv2
import os
 

@api_view(['PUT'])
def obtainFaceEmotionPrediction(request) -> Response:
    if request.method == 'PUT':
        if request.FILES.get("image", None) is not None:
            img = request.FILES["image"]
            img = img.read()

            model = FaceEmotionRecognition()
            img = model.detect_emotion(img)

            dir = '../pictures/faceEmotion/'
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

    
            cv2.imwrite('{}face_emotion_1.png'.format(dir), img)
            return Response({'file': 'face_emotion_1.png'})

    return Response(status="300",data={'file': None})

@api_view(['PUT'])
def obtainMilitaryPrediction(request) -> Response:
    if request.method == 'PUT':
        if request.FILES.get("image", None) is not None:
            img = request.FILES["image"]
            img = img.read()

            model = MilitaryDetector()
            non_military, military = model.military_detector(img)

            dir = '../pictures/militaryDetection/'
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

            non_personnel = []
            personnel = []
            idx = 1

            for person in non_military:
                cv2.imwrite('{}non_military_{}.png'.format(dir, idx), person)
                non_personnel.append('non_military_{}.png'.format(idx))
                idx += 1

            idx = 1
            for person in military:
                cv2.imwrite('{}military_{}.png'.format(dir, idx), person)
                personnel.append('military_{}.png'.format(idx))
                idx += 1

            return Response({'non_military': non_personnel, 'military': personnel})

    return Response({'file': None})