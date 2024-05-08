import face_recognition as fr
import numpy as np


class EncodingCreationError(Exception):
    def __init__(self, message="Failed to create encoding"):
        self.message = message
        super().__init__(self.message)


class Comparison:
    @staticmethod
    def faces_compare(image_array_1, image_array_2, jitters=1) -> float:
        # Загрузка изображений и получение кодировок лиц
        image_1 = np.array(image_array_1)
        image_2 = np.array(image_array_2)

        # Получение кодировок лиц с изображений
        encoding_1 = fr.face_encodings(image_1, num_jitters=jitters, model='large')
        encoding_2 = fr.face_encodings(image_2, num_jitters=jitters, model='large')

        if len(encoding_1) == 0 or len(encoding_2) == 0:
            # Если лица не найдены на одном из изображений
            raise EncodingCreationError

        # Берем первое найденное лицо на каждом изображении
        face_encoding_1 = encoding_1[0]
        face_encoding_2 = encoding_2[0]

        # Сравнение лиц
        face_distance = fr.face_distance([face_encoding_1], face_encoding_2)

        # Преобразуем расстояние в меру схожести от 0 до 1
        similarity = 1 - face_distance[0]  # Чем меньше расстояние, тем ближе к 1, т.е. 0 - наименьшая степень схожести, 1 - наибольшая степень схожести

        return similarity