from dataclasses import dataclass, field
import cv2
from time import sleep
from numpy import isin
from retinaface import RetinaFace

@dataclass
class RetinaFace_HumanDetection:
    _width_crop: int = 20
    _height_crop: int = 60

    def detect_by_image(self, image):
        cropped_bodies = []
        resp = RetinaFace.detect_faces(image)
        
        if isinstance(resp, dict):
            keys = resp.keys()

            for key in keys:
                try:
                    added_height = (resp[key]["facial_area"][3] - resp[key]["facial_area"][1]) * 5 + resp[key]["facial_area"][3]
                    extracted_width_left = resp[key]["facial_area"][0] - (resp[key]["facial_area"][2] - resp[key]["facial_area"][0])
                    added_width_right = resp[key]["facial_area"][2] + (resp[key]["facial_area"][2] - resp[key]["facial_area"][0])

                    if added_height >= image.shape[0]:
                        added_height = image.shape[0] - 1
                    if extracted_width_left < 1:
                        extracted_width_left = 1
                    if added_width_right >= image.shape[1]:
                        added_width_right = image.shape[1] - 1

                    cropped_bodies.append(image[resp[key]["facial_area"][1]:added_height, extracted_width_left:added_width_right])
                except:
                    print("Error when cropping the body")

        return cropped_bodies