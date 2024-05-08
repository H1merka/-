# recfacelib #

## Что это? ##
Этот репозиторий позволяет вам легко считывать лица людей с фотографий и сравнивать их


----------


### Использование ###


Сначала нужно создать экземпляр класса Photo и передать в него путь к фотографии:

    photo = Photo('imgs/example.jpg')


Затем вызовите метод `find_face(min_size, draw_rects)` у экземпляра.
`min_size` - ограничение на размеры лиц в пикселях.
`draw_rects` - рисовать или нет прямоугольники вокруг найденных лиц на фото в экземпляре Photo:

    faces = photo.find_face((40, 50), True)


Метод `show_img(name, scale)` позволяет вывести изображение в отдельном окне.
`name` - имя окна, обязательный параметр.
`scale` - масштаб изображения, умножает размеры изображения на число, необязательный параметр.

    photo.show_img('my_pic', 0.25)


Метод `faces_compare(image_array_1, image_array_2, jitters=30)` сравнивает лица и возвращает результат в виде float.
`image_array_1`, `image_array_2` - элементы результата работы `find_face()`.
`jitters` - точность сравнения, чем больше - тем дольше выполняется и тем больше нагрузка на среду выполнения.


    Comparison.faces_compare(faces[0], faces[1], 50)


----------


## Команда разработчиков ##
Ссылка GitHub: [link](https://github.com/H1merka/Face_recognition) 