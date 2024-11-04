"""
Метод Пауэлла
ЗДЕСЬ ТОЧНОСТЬ МИНИМАЛЬНАЯ EPS = 10^-13 благодаря Decimal (если бы был float, было бы 10^-6)
"""

import math
import decimal
from decimal import Decimal

# 3 задачи на выбор
def f_1(x):  # входная функция № 1
    return ((x + Decimal("1")) * (x + Decimal("4")) ** Decimal("3"))
def f_2(x):  # входная функция № 2
    return (x ** Decimal("2") - Decimal(str(math.sin(x))))
def f_3(x):  # входная функция № 3
    return (x ** Decimal("4") + Decimal("8") * x ** Decimal("3") - Decimal("6") * x ** Decimal("2")
            - Decimal("72") * x + Decimal("90"))
a_1, b_1 = Decimal("-2"), Decimal("-1")  # входные данные № 1
a_2, b_2 = Decimal("0"), Decimal(str(math.pi)) / Decimal("2")  # входные данные № 2
a_3, b_3 = Decimal("1.5"), Decimal("2")  # входная функция № 3

# пользователь выбирает задачу
print("Выберите функцию и отрезок, для которых будет искаться т. min и min методом Пауэлла:")
print("№1: f(x) = (x + 1) * (x + 4) ^ 3; [-2; -1]")
print("№2: f(x) = x ^ 2 - sin(x); [0; pi/2]")
print("№3: f(x) = x ^ 4 + 8 * x ^ 3 - 6 * x ^ 2 - 72 * x + 90; [1,5; 2]")
while True:
    try:
        number_choice = int(input("Введите число 1, 2 или 3: "))
    except ValueError:
        print("Вы ввели не число - введите ещё раз")
    else:
        if number_choice not in (1, 2, 3):
            print("Вы ввели число, отличное от 1, 2 или 3 - введите ещё раз")
        else:
            if number_choice == 1:
                f, a, b = f_1, a_1, b_1
                print("Решаемая задача: f(x) = (x + 1) * (x + 4) ^ 3; [-2; -1]")
            elif number_choice == 2:
                f, a, b = f_2, a_2, b_2
                print("Решаемая задача: f(x) = x ^ 2 - sin(x); [0; pi/2]")
            else:
                f, a, b = f_3, a_3, b_3
                print("Решаемая задача: f(x) = x ^ 4 + 8 * x ^ 3 - 6 * x ^ 2 - 72 * x + 90; [1,5; 2]")
            break

# пользователь вводит точность
print("\nВведите точность eps от 10^-13 до 10^-1 в формате [0.0...0[ненулевое число]], например: eps = 0.001")
print("Для точности eps < 10^-13 решение задачи невозможно в силу ограниченных вычислительных возможностей Python.")
while True:
    try:
        eps_str = input("eps = ")
        eps = Decimal(eps_str)
    except decimal.InvalidOperation:
        print("Вы ввели не число - введите ещё раз")
    else:
        if not (Decimal("0.0000000000001") <= eps <= Decimal("0.1")):
            print("Вы ввели число вне диапазона [10^-13; 10^-1] - введите ещё раз")
        elif eps_str.count('0') != (len(eps_str) - 2):
            print("Вы ввели число не в формате [0.0...0[ненулевое число]] - введите ещё раз")
        else:
            break
eps_signs = len(eps_str) - 2  # столько знаков после точки надо будет оставлять при выводе ответов
print()

# решение задачи методом Пауэлла
x_1, h = a, eps  # задаём сами
while True:
    x_2 = x_1 + h
    f_x_1, f_x_2 = f(x_1), f(x_2)
    if f(x_1) > f(x_2):
        x_3 = x_1 + Decimal("2") * h
    else:
        x_3 = x_1 - h
    f_x_3 = f(x_3)
    f_min = min(f_x_1, f_x_2, f_x_3)
    if f_x_1 == f_min:
        x_min = x_1
    elif f_x_2 == f_min:
        x_min = x_2
    else:
        x_min = x_3
    a_0 = f_x_1
    a_1 = (f_x_2 - f_x_1) / (x_2 - x_1)
    a_2 = (Decimal("1") / (x_3 - x_2)) * (((f_x_3 - f_x_1) / (x_3 - x_1)) - ((f_x_2 - f_x_1) / (x_2 - x_1)))
    x_stat = ((x_2 + x_1) / Decimal("2")) - (a_1 / (Decimal("2") * a_2))  # !!! здесь x_2 + x_1, а не x_2 - x_1
    f_x_stat = f(x_stat)
    if abs(x_stat - x_min) < eps:
        print("x_min =", x_stat.quantize(Decimal("1." + "0" * eps_signs)), "f_min =",
              f_x_stat.quantize(Decimal("1." + "0" * eps_signs)))
        break
    if f_x_stat < f_min:
        x_1 = x_stat
    else:
        x_1 = x_min
