import bitarray


def copy_bit_str(target, source):
    # Если целевая последовательность пуста, копируются все элементы исходной последовательности.
    if len(target) == 0:
        for i in range(0, len(source)):
            # Расширение целевой последовательности и копирование элементов.
            target.extend([0])
            target[i] = source[i]
    else:
        # В противном случае происходит копирование элементов исходной последовательности в целевую.
        for i in range(0, len(source)):
            target[i] = source[i]


#  побитовое сложение двух битовых массивов
def bit_add(a_orig, b):
    # Создание копии аргумента a_orig.
    a = bitarray.bitarray()
    copy_bit_str(a, a_orig)
    i = len(a) - 1
    while i >= 0:
        j = i - 1
        # Если оба бита a и b равны 1, a[i] становится 0, а следующий бит в a,
        # который равен 1, становится 0 (если есть).
        if a[i] is True and b[i] is True:
            a[i] = False
            while j >= 0 and a[j] is True:
                a[j] = False
                j -= 1
            if j >= 0:
                a[j] = True
        # Если a[i] и b[i] не равны 1, a[i] изменяется на результат
        # логического XOR между a[i] и b[i].
        else:
            a[i] = a[i] ^ b[i]
        i -= 1
    return a


def add_bits(message):
    # Получаем длину сообщения в битах.
    i = len(message)
    # Добавляем единицу в конец сообщения.
    message.extend([1])
    # Вычисляем остаток от деления длины сообщения на 1024.
    ost = i % 1024
    k = 0
    # Добавляем нули до тех пор, пока длина сообщения не станет равной 896 по модулю 1024.
    while len(message) % 1024 != 896:
        k += 1
        message.extend([0])
    # Представляем длину сообщения в бинарном виде и дополняем нулями до 128 бит.
    bin_i = bin(i)
    bai = bitarray.bitarray(bin_i[2:])
    step = 128 - len(bai)
    bai.extend([False] * step)
    # Сдвигаем битовый массив на step позиций вправо.
    bai = bai >> step
    # Добавляем полученный битовый массив в конец сообщения.
    message.extend(bai)
    return message


def define_const():
    # Задаем временную переменную с предварительно определенными константами в шестнадцатеричном формате.
    temp_K = ["428a2f98d728ae22", "7137449123ef65cd", "b5c0fbcfec4d3b2f", "e9b5dba58189dbbc",
            "3956c25bf348b538", "59f111f1b605d019", "923f82a4af194f9b", "ab1c5ed5da6d8118",
            "d807aa98a3030242", "12835b0145706fbe", "243185be4ee4b28c", "550c7dc3d5ffb4e2",
            "72be5d74f27b896f", "80deb1fe3b1696b1", "9bdc06a725c71235", "c19bf174cf692694",
            "e49b69c19ef14ad2", "efbe4786384f25e3", "0fc19dc68b8cd5b5", "240ca1cc77ac9c65",
            "2de92c6f592b0275", "4a7484aa6ea6e483", "5cb0a9dcbd41fbd4", "76f988da831153b5",
            "983e5152ee66dfab", "a831c66d2db43210", "b00327c898fb213f", "bf597fc7beef0ee4",
            "c6e00bf33da88fc2", "d5a79147930aa725", "06ca6351e003826f", "142929670a0e6e70",
            "27b70a8546d22ffc", "2e1b21385c26c926", "4d2c6dfc5ac42aed", "53380d139d95b3df",
            "650a73548baf63de", "766a0abb3c77b2a8", "81c2c92e47edaee6", "92722c851482353b",
            "a2bfe8a14cf10364", "a81a664bbc423001", "c24b8b70d0f89791", "c76c51a30654be30",
            "d192e819d6ef5218", "d69906245565a910", "f40e35855771202a", "106aa07032bbd1b8",
            "19a4c116b8d2d0c8", "1e376c085141ab53", "2748774cdf8eeb99", "34b0bcb5e19b48a8",
            "391c0cb3c5c95a63", "4ed8aa4ae3418acb", "5b9cca4f7763e373", "682e6ff3d6b2b8a3",
            "748f82ee5defb2fc", "78a5636f43172f60", "84c87814a1f0ab72", "8cc702081a6439ec",
            "90befffa23631e28", "a4506cebde82bde9", "bef9a3f7b2c67915", "c67178f2e372532b",
            "ca273eceea26619c", "d186b8c721c0c207", "eada7dd6cde0eb1e", "f57d4f7fee6ed178",
            "06f067aa72176fba", "0a637dc5a2c898a6", "113f9804bef90dae", "1b710b35131c471b",
            "28db77f523047d84", "32caab7b40c72493", "3c9ebe0a15c9bebc", "431d67c49c100d4c",
            "4cc5d4becb3e42b6", "597f299cfc657e2a", "5fcb6fab3ad6faec", "6c44198c4a475817"]
    print(len(temp_K))
    # Инициализируем пустой список для констант K.
    K = []
    # Преобразуем каждую шестнадцатеричную строку в bitarray и добавляем в список K.
    for elem in temp_K:
        ba = bitarray.bitarray()
        ba.frombytes(bytes.fromhex(elem))
        K.append(ba)

    # Задаем начальные значения хэш-значений H0-H7.
    H0 = bitarray.bitarray()
    H0.frombytes(bytes.fromhex("6a09e667f3bcc908"))
    H1 = bitarray.bitarray()
    H1.frombytes(bytes.fromhex("bb67ae8584caa73b"))
    H2 = bitarray.bitarray()
    H2.frombytes(bytes.fromhex("3c6ef372fe94f82b"))
    H3 = bitarray.bitarray()
    H3.frombytes(bytes.fromhex("a54ff53a5f1d36f1"))
    H4 = bitarray.bitarray()
    H4.frombytes(bytes.fromhex("510e527fade682d1"))
    H5 = bitarray.bitarray()
    H5.frombytes(bytes.fromhex("9b05688c2b3e6c1f"))
    H6 = bitarray.bitarray()
    H6.frombytes(bytes.fromhex("1f83d9abfb41bd6b"))
    H7 = bitarray.bitarray()
    H7.frombytes(bytes.fromhex("5be0cd19137e2179"))

    # Возвращаем все константы K и хэш-значения H0-H7.
    return K, H0, H1, H2, H3, H4, H5, H6, H7


# Функция сдвигает значение x на n битов вправо.
def shr(x, n):
    return x >> n


# Функция выполняет циклический сдвиг значения x на n битов вправо.
def rotr(x, n):
    return (x >> n) | (x << (64 - n))


# Функция выполняет циклический сдвиг значения x на n битов влево.
def rotl(x, n):
    return (x << n) | (x >> (64 - n))


# Функция "choice": для каждого бита результата выбирает бит из y или z,
# в зависимости от значения бита в x.
def ch(x, y, z):
    return (x & y) ^ (~x & z)


# Функция возвращает бит четности (xor) для трех значений x, y и z.
def parity(x, y, z):
    return x ^ y ^ z


# Функция возвращает бит мажоритарности (majority) для трех значений x, y и z.
def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


# Функция выбирает подходящую операцию в зависимости от значения t.
def fun(x, y, z, t):
    res = -1
    if 0 <= t <= 19:
        res = ch(x, y, z)
    elif 20 <= t <= 39 | 60 <= t <= 79:
        res = parity(x, y, z)
    elif 40 <= t <= 59:
        res = maj(x, y, z)
    return res


# Функция возвращает результат применения раундовой функции к значению x для раунда 0.
def summ0(x):
    return rotr(x, 28) ^ rotr(x, 34) ^ rotr(x, 39)


# Функция возвращает результат применения раундовой функции к значению x для раунда 1.
def summ1(x):
    return rotr(x, 14) ^ rotr(x, 18) ^ rotr(x, 41)


# Функция возвращает результат применения сигмы к значению x для сигмы 0.
def sigma0(x):
    return rotr(x, 1) ^ rotr(x, 8) ^ shr(x, 7)


# Функция возвращает результат применения сигмы к значению x для сигмы 1.
def sigma1(x):
    return rotr(x, 19) ^ rotr(x, 61) ^ shr(x, 6)


def work(message):
    # Инициализация констант, используемых в алгоритме хеширования.
    K, H0, H1, H2, H3, H4, H5, H6, H7 = define_const()
    # Перебор блоков сообщения.
    for i in range(0, len(message) // 1024):
        W = []
        # Формирование массива W из 16 слов по 64 бита каждое.
        for t in range(0, 16):
            W.append(message[t * 64 + (i * 1024):t * 64 + 64 + (i * 1024)])
        # Расширение массива W до 80 слов.
        for t in range(16, 80):
            W.append(bit_add(bit_add(sigma1(W[t - 2]), W[t - 7]), bit_add(sigma0(W[t - 15]), W[t - 16])))
        # Инициализация переменных a, b, c, d, e, f, g, h.
        a = bitarray.bitarray()
        b = bitarray.bitarray()
        c = bitarray.bitarray()
        d = bitarray.bitarray()
        e = bitarray.bitarray()
        f = bitarray.bitarray()
        g = bitarray.bitarray()
        h = bitarray.bitarray()

        # Копирование значений хеш-констант в переменные a, b, c, d, e, f, g, h.
        copy_bit_str(a, H0)
        copy_bit_str(b, H1)
        copy_bit_str(c, H2)
        copy_bit_str(d, H3)
        copy_bit_str(e, H4)
        copy_bit_str(f, H5)
        copy_bit_str(g, H6)
        copy_bit_str(h, H7)

        # Цикл сжатия для каждого слова массива W.
        for t in range(0, 80):
            # Вычисление промежуточных значений T1 и T2.
            HSumm = bit_add(h, summ1(e))
            KW = bit_add(K[t], W[t])
            CHKW = bit_add(ch(e, f, g), KW)
            T1 = bit_add(HSumm, CHKW)
            T2 = bit_add(summ0(a), maj(a, b, c))
            # Обновление значений переменных a, b, c, d, e, f, g, h.
            copy_bit_str(h, g)
            copy_bit_str(g, f)
            copy_bit_str(f, e)
            copy_bit_str(e, bit_add(d, T1))
            copy_bit_str(d, c)
            copy_bit_str(c, b)
            copy_bit_str(b, a)
            copy_bit_str(a, bit_add(T1, T2))
        # Обновление значений хеш-констант.
        H0 = bit_add(H0, a)
        H1 = bit_add(H1, b)
        H2 = bit_add(H2, c)
        H3 = bit_add(H3, d)
        H4 = bit_add(H4, e)
        H5 = bit_add(H5, f)
        H6 = bit_add(H6, g)
        H7 = bit_add(H7, h)

        # print("end iter")
    # Вывод результирующего хеш-значения.
    print("result: ", H0.tobytes().hex(), H1.tobytes().hex(), H2.tobytes().hex(), H3.tobytes().hex(),
          H4.tobytes().hex(), H5.tobytes().hex(), H6.tobytes().hex(), H7.tobytes().hex())
    # Возвращает список из восьми результирующих хеш-значений в шестнадцатеричном формате.
    return [H0.tobytes().hex(), H1.tobytes().hex(), H2.tobytes().hex(), H3.tobytes().hex(),
          H4.tobytes().hex(), H5.tobytes().hex(), H6.tobytes().hex(), H7.tobytes().hex()]


def get_difference(Fmessage, Smessage):
    # Выводит количество хеш-значений в переданных сообщениях.
    print(len(Fmessage))
    # Инициализация счетчика для подсчета различий между хеш-значениями.
    count = 0
    # Перебор всех хеш-значений в каждом сообщении.
    for i in range(0, len(Fmessage)):
        for j in range(0, len(Fmessage[i])):
            # Увеличивает счетчик, если соответствующие биты двух хеш-значений различны.
            count += Fmessage[i][j] != Smessage[i][j]
            # Альтернативный способ подсчета:
            # if Fmessage[i][j] != Smessage[i][j]:
            #     count = count + 1
    # Возвращает общее количество различных битов в двух сообщениях.
    return count


def get_law_effect(message, n):
    # Инициализация переменных K, H0-H7 значениями из констант, определенных в другой функции.
    K, H0, H1, H2, H3, H4, H5, H6, H7 = define_const()
    # Создание списка для хранения различий между двумя хеш-значениями.
    dif = []
    # Создание переменных для альтернативного сообщения и копирования начальных значений хеш-значений.
    alternative_message = bitarray.bitarray()
    H20 = bitarray.bitarray()
    H21 = bitarray.bitarray()
    H22 = bitarray.bitarray()
    H23 = bitarray.bitarray()
    H24 = bitarray.bitarray()
    H25 = bitarray.bitarray()
    H26 = bitarray.bitarray()
    H27 = bitarray.bitarray()
    copy_bit_str(H20, H0)
    copy_bit_str(H21, H1)
    copy_bit_str(H22, H2)
    copy_bit_str(H23, H3)
    copy_bit_str(H24, H4)
    copy_bit_str(H25, H5)
    copy_bit_str(H26, H6)
    copy_bit_str(H27, H7)
    # Для каждого индекса num из списка n создается альтернативное сообщение с измененным битом на позиции num.
    for k, num in enumerate(n):
        copy_bit_str(alternative_message, message)
        alternative_message[num] = alternative_message[num] == False
        # Для каждого блока данных размером 1024 бита выполняются основные операции алгоритма SHA-512.
        for i in range(0, len(message) // 1024):
            W = []
            W2 = []
            for t in range(0, 16):
                # print("append W: ", t * 64 + (i * 1024), t * 64 + 64 + (i * 1024))
                W.append(message[t * 64 + (i * 1024):t * 64 + 64 + (i * 1024)])
                W2.append(alternative_message[t * 64 + (i * 1024):t * 64 + 64 + (i * 1024)])
                # print(W[len(W) - 1])
            for t in range(16, 80):
                W.append(bit_add(bit_add(sigma1(W[t - 2]), W[t - 7]), bit_add(sigma0(W[t - 15]), W[t - 16])))
                W2.append(bit_add(bit_add(sigma1(W2[t - 2]), W2[t - 7]), bit_add(sigma0(W2[t - 15]), W2[t - 16])))
            # Инициализация переменных a-h для текущего блока данных и альтернативного сообщения.
            # Переменные a2-h2 используются для альтернативного сообщения.
            # Каждая переменная представляет собой 32-битное хеш-значение.
            a = bitarray.bitarray()
            b = bitarray.bitarray()
            c = bitarray.bitarray()
            d = bitarray.bitarray()
            e = bitarray.bitarray()
            f = bitarray.bitarray()
            g = bitarray.bitarray()
            h = bitarray.bitarray()

            a2 = bitarray.bitarray()
            b2 = bitarray.bitarray()
            c2 = bitarray.bitarray()
            d2 = bitarray.bitarray()
            e2 = bitarray.bitarray()
            f2 = bitarray.bitarray()
            g2 = bitarray.bitarray()
            h2 = bitarray.bitarray()

            copy_bit_str(a, H0)
            copy_bit_str(b, H1)
            copy_bit_str(c, H2)
            copy_bit_str(d, H3)
            copy_bit_str(e, H4)
            copy_bit_str(f, H5)
            copy_bit_str(g, H6)
            copy_bit_str(h, H7)

            copy_bit_str(a2, H20)
            copy_bit_str(b2, H21)
            copy_bit_str(c2, H22)
            copy_bit_str(d2, H23)
            copy_bit_str(e2, H24)
            copy_bit_str(f2, H25)
            copy_bit_str(g2, H26)
            copy_bit_str(h2, H27)

            # Для каждого слова t от 0 до 79 выполняются основные операции алгоритма SHA-512.
            for t in range(0, 80):
                HSumm = bit_add(h, summ1(e))
                KW = bit_add(K[t], W[t])
                CHKW = bit_add(ch(e, f, g), KW)
                T1 = bit_add(HSumm, CHKW)
                T2 = bit_add(summ0(a), maj(a, b, c))
                copy_bit_str(h, g)
                copy_bit_str(g, f)
                copy_bit_str(f, e)
                copy_bit_str(e, bit_add(d, T1))
                copy_bit_str(d, c)
                copy_bit_str(c, b)
                copy_bit_str(b, a)
                copy_bit_str(a, bit_add(T1, T2))

                HSumm = bit_add(h2, summ1(e2))
                KW = bit_add(K[t], W2[t])
                CHKW = bit_add(ch(e2, f2, g2), KW)
                T1 = bit_add(HSumm, CHKW)
                T2 = bit_add(summ0(a2), maj(a2, b2, c2))
                copy_bit_str(h2, g2)
                copy_bit_str(g2, f2)
                copy_bit_str(f2, e2)
                copy_bit_str(e2, bit_add(d2, T1))
                copy_bit_str(d2, c2)
                copy_bit_str(c2, b2)
                copy_bit_str(b2, a2)
                copy_bit_str(a2, bit_add(T1, T2))

                dif.append(get_difference([a, b, c, d, e, f, g, h], [a2, b2, c2, d2, e2, f2, g2, h2]))

            H0 = bit_add(H0, a)
            H1 = bit_add(H1, b)
            H2 = bit_add(H2, c)
            H3 = bit_add(H3, d)
            H4 = bit_add(H4, e)
            H5 = bit_add(H5, f)
            H6 = bit_add(H6, g)
            H7 = bit_add(H7, h)

            H20 = bit_add(H20, a2)
            H21 = bit_add(H21, b2)
            H22 = bit_add(H22, c2)
            H23 = bit_add(H23, d2)
            H24 = bit_add(H24, e2)
            H25 = bit_add(H25, f2)
            H26 = bit_add(H26, g2)
            H27 = bit_add(H27, h2)

            print("different count = ", dif)

            # print("end iter")
    print("result: ", H0.tobytes().hex(), H1.tobytes().hex(), H2.tobytes().hex(), H3.tobytes().hex(),
          H4.tobytes().hex(), H5.tobytes().hex(), H6.tobytes().hex(), H7.tobytes().hex())
    print("result: ", H20.tobytes().hex(), H21.tobytes().hex(), H22.tobytes().hex(), H23.tobytes().hex(),
          H24.tobytes().hex(), H25.tobytes().hex(), H26.tobytes().hex(), H27.tobytes().hex())

    return [dif, [H0.tobytes().hex(), H1.tobytes().hex(), H2.tobytes().hex(), H3.tobytes().hex(),
          H4.tobytes().hex(), H5.tobytes().hex(), H6.tobytes().hex(), H7.tobytes().hex()],
            [H20.tobytes().hex(), H21.tobytes().hex(), H22.tobytes().hex(), H23.tobytes().hex(),
          H24.tobytes().hex(), H25.tobytes().hex(), H26.tobytes().hex(), H27.tobytes().hex()]]


def get_law_effect_many(message, n):
    # Определение констант и начальных значений хеш-функции
    K, H0, H1, H2, H3, H4, H5, H6, H7 = define_const()

    # Создание списка для хранения различий между хеш-значениями
    dif = []

    # Создание копий хеш-значений и исходного сообщения для альтернативной обработки
    alternative_message = bitarray.bitarray()
    H20 = bitarray.bitarray()
    H21 = bitarray.bitarray()
    H22 = bitarray.bitarray()
    H23 = bitarray.bitarray()
    H24 = bitarray.bitarray()
    H25 = bitarray.bitarray()
    H26 = bitarray.bitarray()
    H27 = bitarray.bitarray()
    copy_bit_str(H20, H0)
    copy_bit_str(H21, H1)
    copy_bit_str(H22, H2)
    copy_bit_str(H23, H3)
    copy_bit_str(H24, H4)
    copy_bit_str(H25, H5)
    copy_bit_str(H26, H6)
    copy_bit_str(H27, H7)
    copy_bit_str(alternative_message, message)

    # Инвертирование битов в альтернативном сообщении по индексам из списка n
    for k, num in enumerate(n):
        # copy_bit_str(alternative_message, message)
        print("Before = ", num, alternative_message[num])
        alternative_message[num] = alternative_message[num] == False
        print("After = ", num, alternative_message[num])

    # Цикл обработки блоков данных по 1024 бита
    for i in range(0, len(message) // 1024):
        W = []
        W2 = []

        # Разбиение блока данных на слова по 64 бита
        for t in range(0, 16):
            # print("append W: ", t * 64 + (i * 1024), t * 64 + 64 + (i * 1024))
            W.append(message[t * 64 + (i * 1024):t * 64 + 64 + (i * 1024)])
            W2.append(alternative_message[t * 64 + (i * 1024):t * 64 + 64 + (i * 1024)])
            # print(W[len(W) - 1])

        # Дополнение слов для расширения до 80 слов
        for t in range(16, 80):
            W.append(bit_add(bit_add(sigma1(W[t - 2]), W[t - 7]), bit_add(sigma0(W[t - 15]), W[t - 16])))
            W2.append(bit_add(bit_add(sigma1(W2[t - 2]), W2[t - 7]), bit_add(sigma0(W2[t - 15]), W2[t - 16])))

        # Инициализация переменных для хранения промежуточных результатов
        a = bitarray.bitarray()
        b = bitarray.bitarray()
        c = bitarray.bitarray()
        d = bitarray.bitarray()
        e = bitarray.bitarray()
        f = bitarray.bitarray()
        g = bitarray.bitarray()
        h = bitarray.bitarray()

        a2 = bitarray.bitarray()
        b2 = bitarray.bitarray()
        c2 = bitarray.bitarray()
        d2 = bitarray.bitarray()
        e2 = bitarray.bitarray()
        f2 = bitarray.bitarray()
        g2 = bitarray.bitarray()
        h2 = bitarray.bitarray()

        # Копирование значений хеш-функции для обеих версий сообщения
        copy_bit_str(a, H0)
        copy_bit_str(b, H1)
        copy_bit_str(c, H2)
        copy_bit_str(d, H3)
        copy_bit_str(e, H4)
        copy_bit_str(f, H5)
        copy_bit_str(g, H6)
        copy_bit_str(h, H7)

        copy_bit_str(a2, H20)
        copy_bit_str(b2, H21)
        copy_bit_str(c2, H22)
        copy_bit_str(d2, H23)
        copy_bit_str(e2, H24)
        copy_bit_str(f2, H25)
        copy_bit_str(g2, H26)
        copy_bit_str(h2, H27)

        # Основной цикл алгоритма хеширования
        for t in range(0, 80):
            # Вычисление временной переменной HSumm как суммы текущего значения h и преобразования e.
            HSumm = bit_add(h, summ1(e))
            # Вычисление временной переменной KW как суммы текущего значения ключа K и текущего слова данных W.
            KW = bit_add(K[t], W[t])
            # Вычисление временной переменной CHKW как суммы преобразования CH и KW.
            CHKW = bit_add(ch(e, f, g), KW)
            # Вычисление временной переменной T1 как суммы HSumm и CHKW.
            T1 = bit_add(HSumm, CHKW)
            # Вычисление временной переменной T2 как суммы преобразования Sigma0 и Maj.
            T2 = bit_add(summ0(a), maj(a, b, c))

            # Обновление переменных a до h согласно алгоритму SHA-512.
            copy_bit_str(h, g)
            copy_bit_str(g, f)
            copy_bit_str(f, e)
            copy_bit_str(e, bit_add(d, T1))
            copy_bit_str(d, c)
            copy_bit_str(c, b)
            copy_bit_str(b, a)
            copy_bit_str(a, bit_add(T1, T2))

            # Аналогичные операции для альтернативной переменной с альтернативным сообщением.
            HSumm = bit_add(h2, summ1(e2))
            KW = bit_add(K[t], W2[t])
            CHKW = bit_add(ch(e2, f2, g2), KW)
            T1 = bit_add(HSumm, CHKW)
            T2 = bit_add(summ0(a2), maj(a2, b2, c2))
            copy_bit_str(h2, g2)
            copy_bit_str(g2, f2)
            copy_bit_str(f2, e2)
            copy_bit_str(e2, bit_add(d2, T1))
            copy_bit_str(d2, c2)
            copy_bit_str(c2, b2)
            copy_bit_str(b2, a2)
            copy_bit_str(a2, bit_add(T1, T2))

        # Обновление хеш-значений H0 до H7 и H20 до H27.
        H0 = bit_add(H0, a)
        H1 = bit_add(H1, b)
        H2 = bit_add(H2, c)
        H3 = bit_add(H3, d)
        H4 = bit_add(H4, e)
        H5 = bit_add(H5, f)
        H6 = bit_add(H6, g)
        H7 = bit_add(H7, h)

        H20 = bit_add(H20, a2)
        H21 = bit_add(H21, b2)
        H22 = bit_add(H22, c2)
        H23 = bit_add(H23, d2)
        H24 = bit_add(H24, e2)
        H25 = bit_add(H25, f2)
        H26 = bit_add(H26, g2)
        H27 = bit_add(H27, h2)

        # Вычисление различий между H0-H7 и H20-H27 и добавление их в список dif.
        dif.append(get_difference([H0, H1, H2, H3, H4, H5, H6, H7], [H20, H21, H22, H23, H24, H25, H26, H27]))
        # Вывод количества различий.
        print("different count = ", dif)

        # print("end iter")
    # Вывод результатов хеширования.
    print("result: ", H0.tobytes().hex(), H1.tobytes().hex(), H2.tobytes().hex(), H3.tobytes().hex(),
          H4.tobytes().hex(), H5.tobytes().hex(), H6.tobytes().hex(), H7.tobytes().hex())
    print("result: ", H20.tobytes().hex(), H21.tobytes().hex(), H22.tobytes().hex(), H23.tobytes().hex(),
          H24.tobytes().hex(), H25.tobytes().hex(), H26.tobytes().hex(), H27.tobytes().hex())
    # Возврат списка, содержащего различия и конечные хеш-значения.
    return [dif, [H0.tobytes().hex(), H1.tobytes().hex(), H2.tobytes().hex(), H3.tobytes().hex(),
          H4.tobytes().hex(), H5.tobytes().hex(), H6.tobytes().hex(), H7.tobytes().hex()],
            [H20.tobytes().hex(), H21.tobytes().hex(), H22.tobytes().hex(), H23.tobytes().hex(),
          H24.tobytes().hex(), H25.tobytes().hex(), H26.tobytes().hex(), H27.tobytes().hex()]]
