"""
Метод Пауэлла
ЗДЕСЬ ТОЧНОСТЬ МИНИМАЛЬНАЯ EPS = 10^-13 благодаря Decimal (если бы был float, было бы 10^-6)
"""

import math
import decimal
from decimal import Decimal
import prettytable

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
print("Выберите функцию и отрезок, для которых будет искаться т. min и min в ней методом Пауэлла:")
print("Задача №1: f(x) = (x + 1) * (x + 4) ^ 3; [-2; -1]")
print("Задача №2: f(x) = x ^ 2 - sin(x); [0; pi/2]")
print("Задача №3: f(x) = x ^ 4 + 8 * x ^ 3 - 6 * x ^ 2 - 72 * x + 90; [1,5; 2]")
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
iter = 0
table = prettytable.PrettyTable()
table.field_names = ["n", "x1", "x2", "x3", "f(x1)", "f(x2)", "f(x3)", "a0", "a1", "a2", "x_min", "f(x_min)",
                     "x*", "f(x*)", "eps_n"]
while True:
    iter += 1
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
    eps_n = abs(x_stat - x_min)
    table.add_row([iter, f"{x_1:.{eps_signs}f}", f"{x_2:.{eps_signs}f}", f"{x_3:.{eps_signs}f}",
                   f"{f_x_1:.{eps_signs}f}", f"{f_x_2:.{eps_signs}f}", f"{f_x_3:.{eps_signs}f}", f"{a_0:.{eps_signs}f}",
                   f"{a_1:.{eps_signs}f}", f"{a_2:.{eps_signs}f}", f"{x_min:.{eps_signs}f}", f"{f_min:.{eps_signs}f}",
                   f"{x_stat:.{eps_signs}f}", f"{f_x_stat:.{eps_signs}f}", f"{eps_n:.{eps_signs}f}"])
    if eps_n < eps:
        break
    if f_x_stat < f_min:
        x_1 = x_stat
    else:
        x_1 = x_min

# вывод ответа
print("Полная таблица расчётов:")
print(table)
x_min_answer, f_min_answer = x_stat, f_x_stat
print(f"\nИтог: точка минимума x_min = {x_min_answer:.{eps_signs}f} и минимум f_min = {f_min_answer:.{eps_signs}f}")
input()  # чтобы консоль не закрылась
