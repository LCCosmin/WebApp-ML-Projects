from dataclasses import dataclass, field
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2


@dataclass(kw_only=True)
class MilitaryPersonnelModel:
    _width_crop: int = 20
    _height_crop: int = 60
    _epochs_no: int = 256
    _batch_size: int = 32
    _checkpoint_path: str = field(init=False)

    def __post_init__(self) -> None:
        self._checkpoint_path = "./ml_models_class/military_detection/brain/cp.ckpt"

    def normalize(self, img):
        img = cv2.resize(img, (self._width_crop, self._height_crop), interpolation = cv2.INTER_AREA)
        img = cv2.GaussianBlur(img, (1,1), 0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        img = img / 255
        #img = cv2.Canny(img, 10, 255)

        return img

    def create_model(self):
        model = tf.keras.models.Sequential([
            keras.layers.InputLayer(input_shape=(self._width_crop * self._height_crop,)),
            keras.layers.Dense(400, activation = 'relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            keras.layers.Dropout(0.1),
            keras.layers.Dense(200, activation = 'relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            keras.layers.Dropout(0.1),
            keras.layers.Dense(100, activation = 'relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            keras.layers.Dropout(0.1),
            keras.layers.Dense(50, activation = 'relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
            keras.layers.Dropout(0.1),
            
            keras.layers.Dense(2, activation = 'sigmoid')
            ])
        
        model.compile(optimizer = 'adam', 
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics = ['accuracy'])

        return model

    def evaluate_image(self, image):
        model = self.create_model()
        model.load_weights(self._checkpoint_path).expect_partial()

        non_military = []
        military = []

        for person in image:
            copy_image = person
            person = self.normalize(person)
            person = np.array(cv2.resize(person, (self._width_crop, self._height_crop)), dtype = float).reshape(-1, self._width_crop * self._height_crop)
            
            predictions = model.predict(person)
            if predictions[0][0] <= 0.5:
                non_military.append(copy_image)
            else:
                military.append(copy_image)

        return (non_military, military)
            