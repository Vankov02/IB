import bitarray
import logic
import matplotlib.pyplot as plt
import graphic

if __name__ == "__main__":
    # Запуск графического интерфейса для работы с программой
    graphic.begin("source.bin")

    # Открытие файла для чтения в бинарном режиме
    input = open("source.bin", "rb")
    ba = bitarray.bitarray()

    # Заполнение массива битов из файла
    ba.frombytes(input.read())

    # Добавление недостающих битов и выполнение хэширования
    fulled_ba = logic.add_bits(ba)
    logic.work(fulled_ba)

    # Получение закона эффекта множества значений
    result_hash = logic.get_law_effect_many(fulled_ba, [512, 1023])

    data = []

    # Создание списка данных для построения гистограммы
    for i in range(0, result_hash[0][0]):
        data.append(3)

    # Построение гистограммы
    fig, axs = plt.subplots(1, 1)
    n_bins = len(data)
    axs.hist(data, bins=20)
    axs.set_title("count difference")

    # Отображение гистограммы
    plt.show()




