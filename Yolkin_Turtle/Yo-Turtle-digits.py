import turtle
from math import sin
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(2)
t.speed(10)

def main():
        # Запрашиваем число
        x = int(input('Введите число: '))

        # Запрашиваем высоту цифр
        v_digit = int(input('Введите высоту цифр: '))
        length = v_digit

        # заносим цифры числа в список
        C = to_digits(x)
        C.reverse()

        # Выставляем черепашку слевого края листа
        t.penup()
        t.backward(300)

        # Рисуем число
        write_digit(C, v_digit)

        # Прячем черепашку
        t.hideturtle()

def to_digits(n):
        """ ф-я выбирает цифры числа справа налево и записывает в список"""
        S=[]
        while n != 0:
                S = S+[n%10]
                n = n // 10
        return S

def write_digit(C, v):
    """
    Рисуем число с использованием индекса списка цифр числа
    и введённой высоты цифр
    """

    # Формируем список из ф-й рисования цифр
    list_digits = {
                0 : d_zero,
                1 : d_one,
                2 : d_two,
                3 : d_three,
                4 : d_four,
                5 : d_five,
                6 : d_six,
                7 : d_seven,
                8 : d_eight,
                9 : d_nine
                }
    # Для всех цифр числа выполняем ф-ю рисования цифры по её индексу
    for i in range(0,len(C)):
            list_digits[C[i]](v)        # обращаемся к словарю ф-ий
            t.forward(10)               # отступ между цифрами

def d_zero(length):
    """ Рисует цифру 0 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """

    L1 = length/2                       # длина горизонтальной линии
    L2 = (length/2)*2**0.5              # длина диагонали
    B = [0, 90, 90, 90]                 # повороты влево
    A = [L1, L1 * 2, L1, L1 * 2]        # длины частей цифры

    t.pendown()

    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)

    t.penup()
    t.forward(L1)

def d_one(length):
    """ Рисует цифру 1 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """
    L1 = length/2           # длина горизонтальной линии
    L2 = (length/2)*2**0.5  # длина диагонали
    B = [90, 135]           # повороты влево
    A = [L1 * 2, L2]        # длины частей цифры

    t.forward(L1)
    t.pendown()

    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)
    t.penup()

def d_two(length):
    """ Рисует цифру 2 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """
    L1 = length/2           # длина горизонтальной линии
    L2 = (length/2)*2**0.5  # длина диагонали
    B = [180, -135, 45, 90] # повороты влево
    A = [L1, L2, L1, L1]    # длины частей цифры

    t.forward(L1)
    t.pendown()

    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)
    t.penup()

def d_three(length):
    """ Рисует цифру 3 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """
    L1 = length/2            # длина горизонтальной линии
    L2 = (length/2)*2**0.5   # длина диагонали
    B = [45, 135, -135, 135] # повороты влево
    A = [L2, L1, L2, L1]     # длины частей цифры

    t.pendown()

    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)
    t.penup()
    t.forward(L1)

def d_four(length):
    """ Рисует цифру 4 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """
    L1 = length/2               # длина горизонтальной линии
    L2 = (length/2)*2**0.5      # длина диагонали
    B = [90, 180, -90, -90]     # повороты влево
    A = [L1 * 2, L1, L1, L1]    # длины частей цифры

    t.forward(L1)
    t.pendown()

    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)
        t.penup()
    t.penup()

def d_five(length):
    """ Рисует цифру 5 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """
    L1 = length/2               # длина горизонтальной линии
    L2 = (length/2)*2**0.5      # длина диагонали
    B = [0, 90, 90, -90, -90]   # повороты влево
    A = [L1, L1, L1, L1, L1]    # длины частей цифры

    t.pendown()
    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)
    t.penup()
    t.forward(L1)

def d_six(length):
    """ Рисует цифру 6 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """
    L1 = length/2                   # длина горизонтальной линии
    L2 = (length/2)*2**0.5          # длина диагонали
    B = [0, 90, 90, -135, 180, 45]  # повороты влево
    A = [L1, L1, L1, L2, L2, L1]    # длины частей цифры

    t.pendown()

    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)
    t.penup()
    t.forward(L1)

def d_seven(length):
    """ Рисует цифру 7 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """
    L1 = length/2           # длина горизонтальной линии
    L2 = (length/2)*2**0.5  # длина диагонали
    B = [90, -45, 135]      # повороты влево
    A = [L1, L2, L1]        # длины частей цифры

    t.pendown()

    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)
    t.penup()
    t.forward(L1)

def d_eight(length):
        """ Рисует цифру 8 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
        """
        L1 = length/2           # длина горизонтальной линии
        d_zero(length)
        t.left(90)
        t.forward(L1)
        t.left(90)
        t.pendown()
        t.forward(L1)
        t.penup()
        t.backward(L1)
        t.left(90)
        t.forward(L1)
        t.left(90)

def d_nine(length):
    """ Рисует цифру 9 с высотой length
        слева от направления черепахи
        контракт:
            черепаха возвращается в исходную точку
            и исходную ориентацию, а затем выставляется
            в правый нижний угол цифры
            перо оказывается поднятым по окончанию ф-ии
    """
    L1 = length/2               # длина горизонтальной линии
    L2 = (length/2)*2**0.5      # длина диагонали
    B = [45, 45, 90, 90, 90]    # повороты влево
    A = [L2, L1, L1, L1, L1]    # длины частей цифры

    t.pendown()

    # рисуем цифру
    for length, degree in zip(A, B):
        t.left(degree)
        t.forward(length)

    # возврат черепашки
    A.reverse()
    B.reverse()
    for length, degree in zip(A, B):
        t.backward(length)
        t.right(degree)
    t.penup()
    t.forward(L1)

# Основная программа
main()

""" СКИ Черепашка"""
# t.left(30)
# t.rigth(30)
# t.forward(200)
# t.backward(200)
# t.penup()
# t.pendown()
#t.begin_fill()
#t.end_fill()
