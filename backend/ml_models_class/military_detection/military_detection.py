from dataclasses import dataclass
from ml_models_class.military_detection.utils.ImageReader import ImageReader
from ml_models_class.military_detection.ml_model.MilitaryPersonnelModel import MilitaryPersonnelModel
from ml_models_class.military_detection.face_detector.RetinaFaceHumanDetection import RetinaFace

@dataclass
class MilitaryDetector:
    def military_detector(image):
        ImgReader = ImageReader()
        MilitaryModel = MilitaryPersonnelModel()
        RetinaFc = RetinaFace()

        return MilitaryModel.evaluate_image(RetinaFc.detect_by_image(ImgReader.read_by_image(image)))