"""Метод Пауэлла"""

# импортируем необходимые библиотеки
import math, numpy as np, matplotlib.pyplot as plt
from decimal import Decimal
from prettytable import PrettyTable

# 3 функции на выбор:

def f_1(x):  # функция №1: f(x) = (x + 1) * (x + 4) ^ 3
    return (x + Decimal("1")) * (x + Decimal("4")) ** Decimal("3")


def f_2(x):  # функция №2: f(x) = x ^ 2 - sin(x)
    return x ** Decimal("2") - Decimal(math.sin(x))


def f_3(x):  # функция №3: f(x) = x ^ 2 - 3 * x + x * ln(x + 1)
    return x ** Decimal("2") - Decimal("3") * x + x * Decimal(math.log(x + Decimal("1")))


def check_unimodality(func, a, b):  # проверяет унимодальность функции на выбранном начальном отрезке
    if func == f_1:
        func_dxdx = lambda x: Decimal("12") * x ** Decimal("2") + Decimal("78") * x + Decimal("120")
    elif func == f_2:
        func_dxdx = lambda x: Decimal("2") + Decimal(math.sin(x))
    else:
        func_dxdx = lambda x: ((Decimal("2") * x ** Decimal("2") + Decimal("5") * x + Decimal("4")) /
                               ((x + Decimal("1")) ** Decimal("2")))
    # функция унимодальна на [a; b], если её вторая производная >= 0 на [a, b]
    x = np.linspace(a, b, 1000)
    for i in x:
        if func_dxdx(Decimal(i)) < Decimal("0"):
            return False
    return True


def graph_function(func, left, right, x_min = None, f_min = None):
    x = np.linspace(left, right, 1000)
    y = [func(Decimal(i)) for i in x]
    plt.figure(figsize=(9, 5))
    plt.plot(x, y, color="red", label="Исходная функция")
    if x_min == f_min == None:
        title = "Выберите начальный интервал"
    else:
        title = "Графики исходной функции и точки минимума"
        plt.scatter(x_min, f_min, color="black", label="Точка минимума")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()


def get_function():  # пользователь выбирает функцию
    print("Выберите функцию, для которой будет искаться т. min и min в ней методом Пауэлла:")
    print("Задача №1: f(x) = (x + 1) * (x + 4) ^ 3")
    print("Задача №2: f(x) = x ^ 2 - sin(x)")
    print("Задача №3: f(x) = x ^ 2 - 3 * x + x * ln(x + 1)")
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
                    return f_1
                elif number_choice == 2:
                    return f_2
                else:
                    return f_3


def get_interval(func):  # пользователь вводит начальный отрезок
    print("Введите начальный отрезок [a; b]:")
    # выведем пользователю график исходной функции, чтобы он выбрал начальный отрезок
    if func == f_1:  # для функции №1 желательно брать отрезок [-2; -1]
        graph_function(func, -6, 0)
    elif func == f_2:  # для функции №2 желательно брать отрезок [-2; 3]
        graph_function(func, -6, 7)
    else:  # для функции №3 желательно брать отрезок [0; 2]
        graph_function(func, -0.9, 4)
    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))
        except ValueError:
            print("Некорректный ввод: нужно вводить числа")
        else:
            if Decimal(a) >= Decimal(b):
                print("Некорректный ввод: a должно быть меньше b")
            else:
                if func == f_3 and a <= Decimal("-1"):  # проверка области определения для функции №3
                    print("Вышли за область определения функции: повторите ввод")
                elif not check_unimodality(func, a, b):
                    print("Функция не унимодальна на данном интервале: повторите ввод")
                else:
                    return Decimal(a), Decimal(b)


def get_accuracy():  # пользователь вводит точность
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
    return eps, eps_signs


def powell_method(f, a, b, eps, eps_signs):  # метод Пауэлла
    x_1, h = a, eps  # задаём сами
    iter = 0
    table = PrettyTable()
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
        if f_min == f_x_1:
            x_min = x_1
        elif f_min == f_x_2:
            x_min = x_2
        else:
            x_min = x_3
        a_0 = f_x_1
        a_1 = (f_x_2 - f_x_1) / (x_2 - x_1)
        a_2 = (Decimal("1") / (x_3 - x_2)) * (((f_x_3 - f_x_1) / (x_3 - x_1)) - ((f_x_2 - f_x_1) / (x_2 - x_1)))
        x_stat = ((x_2 + x_1) / Decimal("2")) - (a_1 / (Decimal("2") * a_2))
        f_x_stat = f(x_stat)
        eps_n = abs(x_stat - x_min)
        table.add_row([iter, f"{x_1:.{eps_signs}f}", f"{x_2:.{eps_signs}f}", f"{x_3:.{eps_signs}f}",
                       f"{f_x_1:.{eps_signs}f}", f"{f_x_2:.{eps_signs}f}", f"{f_x_3:.{eps_signs}f}",
                       f"{a_0:.{eps_signs}f}",
                       f"{a_1:.{eps_signs}f}", f"{a_2:.{eps_signs}f}", f"{x_min:.{eps_signs}f}",
                       f"{f_min:.{eps_signs}f}",
                       f"{x_stat:.{eps_signs}f}", f"{f_x_stat:.{eps_signs}f}", f"{eps_n:.{eps_signs}f}"])
        if eps_n < eps:
            break
        if f_x_stat < f_min:
            x_1 = x_stat
        else:
            x_1 = x_min

    return x_stat, f_x_stat, table


def main():
    # получаем данные от пользователя
    f = get_function()
    a, b = get_interval(f)
    eps, eps_signs = get_accuracy()
    # применение метода Пауэлла
    x_min, f_min, table = powell_method(f, a, b, eps, eps_signs)
    # вывод ответов
    print("\nПолная таблица расчётов:")
    print(table)
    print(f"\nИтог: точка минимума x_min = {x_min:.{eps_signs}f} и минимум f_min = {f_min:.{eps_signs}f}")
    graph_function(f, a, b, x_min, f_min)  # вывод графика функции с найденной точкой


main()
input()  # чтобы консоль не закрылась
