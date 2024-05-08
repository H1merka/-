import cv2
import dlib
from PIL import Image


class Photo:
    def __init__(self, img_path: str): #img_path - путь к файлу
        self.img = cv2.imread(img_path)
        self.pil_img = Image.open(img_path)
        self.size = self.pil_img.size

    def find_face(self, min_size=(30, 30), draw_rects=False):
        '''
        Метод нахождения лиц на фото.
        min_res - минимальное разрешение лица
        Возвращает класс rectangles.
        '''
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        detector = dlib.get_frontal_face_detector()
        faces = detector(img_gray)
        Photo.check_size(faces, min_size)
        if draw_rects == True:
            Photo.draw_rects(self.img, faces)
        return tuple([self.img[face.top():face.bottom(), face.left():face.right()] for face in faces])

    @staticmethod
    def draw_rects(img, detection):
        '''
        Метод рисования прямоугольников вокруг лиц.
        img - изначальное фото
        detection - результат работы find_face()
        '''
        for face in detection:
            cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (0, 0, 255), 2)

    def show_img(self, name: str, scale=None):
        new_img = self.img
        if scale is not None:
            new_img = cv2.resize(new_img, (int(self.size[0] * scale), int(self.size[1] * scale)))
        cv2.imshow(name, new_img)
        cv2.waitKey()

    @staticmethod
    def check_size(detection, size: tuple):
        filtered_faces = []
        for face in detection:
            if (face.right() - face.left()) >= size[0] or (face.bottom() - face.top()) >= size[1]:
                filtered_faces.append(face)
        return filtered_faces
