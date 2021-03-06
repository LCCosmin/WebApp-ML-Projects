from dataclasses import dataclass, field
import cv2

@dataclass
class ImageReader:
    _image_path: str

    def update_image_path(self, path) -> None:
        self._image_path = path

    def read_by_image(self):
        return self._image_path