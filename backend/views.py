from rest_framework.decorators import api_view
from rest_framework.response import Response
from ml_models_class.face_emotion_detection.face_emotion_detection import FaceEmotionRecognition
from ml_models_class.military_detection.military_detection import MilitaryDetector

@api_view(['PUT'])
def obtainFaceEmotionPrediction(request):
    if request.method == 'PUT':
        print(request.data)
        if request.FILES.get("image", None) is not None:
            img = request.FILES["image"]
            
            model = FaceEmotionRecognition()
            return Response({'file': model.detect_emotion(img)})

    return Response({'file': None})

@api_view(['PUT'])
def obtainMilitaryPrediction(request):
    if request.method == 'PUT':
        if request.data:
            model = MilitaryDetector()
            print(request.data)
            return Response({'file': model.military_detector(request.data)})

    return Response({'file': None})