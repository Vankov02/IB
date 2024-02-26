import os
import logic
import bitarray
import tkinter as tk
import matplotlib.pyplot as plt
import subprocess
from PIL import ImageTk, Image
import tkinter.messagebox as mb


def open_text():
    try:
        current_directory = os.getcwd()  # Получаем текущую директорию
        # Формируем путь к файлу 'source.bin' в текущей директории
        source_path = os.path.join(current_directory, 'source.bin')

        # Запускаем программу Notepad для открытия файла source.bin
        subprocess.Popen(['start', 'notepad', source_path], shell=True)
    except Exception as e:  # Обработка исключений
        # Выводим сообщение об ошибке, если что-то пошло не так при открытии файла
        mb.showerror("Ошибка", f"Невозможно открыть файл: {e}")


def open_hash():
    try:
        current_directory = os.getcwd()  # Получаем текущую директорию
        # Формируем путь к файлу 'ResultHash.txt' в текущей директории
        source_path = os.path.join(current_directory, 'ResultHash.txt')

        # Запускаем программу Notepad для открытия файла ResultHash.txt
        subprocess.Popen(['start', 'notepad', source_path], shell=True)
    except Exception as e:  # Обработка исключений
        # Выводим сообщение об ошибке, если что-то пошло не так при открытии файла
        mb.showerror("Ошибка", f"Невозможно открыть файл: {e}")


def print_error(code):
    msg = ""
    if code == 1:
        msg = "Проблемы с файлом"
    elif code == 2:
        msg = "Операция невозможна"
    mb.showerror("Ошибка", msg)


def define_button(source):
    # Открываем файл для чтения в бинарном режиме
    input = open(source, 'rb')

    # Создаем пустой массив битов
    ba = bitarray.bitarray()

    # Заполняем массив битами из файла
    ba.frombytes(input.read())

    # Добавляем недостающие биты и вычисляем хэш
    fulled_ba = logic.add_bits(ba)
    result_hash = logic.work(fulled_ba)

    # Открываем файл для записи результата хэширования
    output = open('ResultHash.txt', 'w+')

    # Записываем результат хэширования в файл
    for part in result_hash:
        output.write(part)
        output.write(' ')

    # Закрываем файлы
    input.close()

    # Открываем файл с результатом в программе по умолчанию для .txt файлов
    opener = 'start'
    subprocess.call([opener, 'ResultHash.txt'], shell=True)


def define_law_eff_button(source, get_num):
    try:
        print(get_num)  # Выводим на экран переданный аргумент get_num
        values = [int(x) for x in get_num.split(',')]  # Разбиваем строку на числа и преобразуем их в целые числа

        # Открываем файл для чтения в бинарном режиме
        input = open(source, 'rb')
        ba = bitarray.bitarray()

        # Заполняем массив битов из файла
        ba.frombytes(input.read())

        # Добавляем недостающие биты и вычисляем хэш с учетом введенных значений
        fulled_ba = logic.add_bits(ba)
        result_hash = logic.get_law_effect(fulled_ba, values)

        data = []
        print(result_hash[0], get_num)  # Выводим результат хэширования и введенные значения
        # Вычисляем количество вхождений каждого элемента и строим график
        for i, elem in enumerate(result_hash[0]):
            for j in range(0, elem):
                data.append(i)
        plt.plot(result_hash[0])  # Строим график
        print(len(data))  # Выводим общее количество элементов

        # Отображаем график
        plt.show()

    except ValueError:  # Обрабатываем исключение ValueError
        mb.showerror("Ошибка", f" Пустая строка!")  # Выводим сообщение об ошибке в случае пустой строки


def initialization(source):
    # Создание окна приложения
    root = tk.Tk()
    root.title("ИБ Лабораторная работа 1")

    # Загрузка изображения фона
    img = Image.open("bg9try.jpg")
    width = 500

    # Изменение размера изображения с сохранением пропорций
    ratio = (width / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    imag = img.resize((width, height), Image.LANCZOS)
    image = ImageTk.PhotoImage(imag)

    # Добавление изображения на верхнюю часть окна
    tk.Label(root, image=image).pack(side="top", fill="both", expand=0)

    # Создание поля ввода и кнопок для вызова функций
    p_entry = tk.Entry(root, bd=5)
    p_entry.pack()

    tk.Button(root, text="Исследовать\nлавинный эффект", command=lambda: define_law_eff_button(source, p_entry.get()),
              activebackground="black").place(x=200, y=10)
    tk.Button(root, text="Выполнить\nхеширование", command=lambda: define_button(source),
              activebackground="black").place(x=215, y=80)
    tk.Button(root, text="Изменить текст\nдля хеширования", command=open_text,
              activebackground="black").place(x=200, y=150)
    tk.Button(root, text="Посмотреть/Изменить\nХеш", command=open_hash,
              activebackground="black").place(x=190, y=220)

    # Запуск основного цикла приложения
    root.mainloop()


# Функция begin() вызывает функцию initialization() с переданным источником
def begin(source):
    initialization(source)

