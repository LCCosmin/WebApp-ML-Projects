from dataclasses import dataclass
from ml_models_class.military_detection.utils.ImageReader import ImageReader
from ml_models_class.military_detection.ml_model.MilitaryPersonnelModel import MilitaryPersonnelModel
from ml_models_class.military_detection.face_detector.RetinaFaceHumanDetection import RetinaFace_HumanDetection
import cv2
import numpy as np

@dataclass
class MilitaryDetector:
    def military_detector(self, image):
        image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_UNCHANGED)
        ImgReader = ImageReader(image)
        MilitaryModel = MilitaryPersonnelModel()
        RetinaFc = RetinaFace_HumanDetection()

        return MilitaryModel.evaluate_image(RetinaFc.detect_by_image(ImgReader.read_by_image()))