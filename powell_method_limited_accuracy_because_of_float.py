# Метод Пауэлла
# ЗДЕСЬ ТОЧНОСТЬ МИНИМАЛЬНАЯ EPS = 10^-6 из-за float
import math
def f(x):  # входная функция № 1
    return ((x + 1) * (x + 4) ** 3)
# def f(x):  # входная функция № 2
#     return (x ** 2 - math.sin(x))
# def f(x):  # входная функция № 3
#     return (x ** 4 + 8 * x ** 3 - 6 * x ** 2 - 72 * x + 90)


a, b = -2, -1  # входные данные № 1
# a, b = 0, math.pi / 2  # входные данные № 2
# a, b = 1.5, 2  # входная функция № 3

print("\nВведите точность eps от 10^-6 до 10^-1 в формате [0.0...0[ненулевое число]], например: eps = 0.001")
print("Для точности eps < 10^-6 решение задачи невозможно в силу ограниченных вычислительных возможностей Python.")
while True:
    try:
        eps_str = input("eps = ")
        eps = float(eps_str)
    except ValueError:
        print("Вы ввели не число - введите ещё раз")
    else:
        if not (10**(-6) <= eps <= 10**(-1)):
            print("Вы ввели число вне диапазона [10^-6; 10^-1] - введите ещё раз")
        elif eps_str.count('0') != (len(eps_str) - 2):
            print("Вы ввели число не в формате [0.0...0[ненулевое число]] - введите ещё раз")
        else:
            break
eps_signs = len(eps_str) - 2  # столько знаков после точки надо будет оставлять при выводе ответов

x_1, h = a, eps  # задаём сами
while True:
    x_2 = x_1 + h
    f_x_1, f_x_2 = f(x_1), f(x_2)
    if f(x_1) > f(x_2):
        x_3 = x_1 + 2 * h
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
    a_2 = (1 / (x_3 - x_2)) * (((f_x_3 - f_x_1) / (x_3 - x_1)) - ((f_x_2 - f_x_1) / (x_2 - x_1)))
    if a_2 == 0:
        k = 1
    x_stat = ((x_2 + x_1) / 2) - (a_1 / (2 * a_2))  # !!! здесь x_2 + x_1, а не x_2 - x_1
    f_x_stat = f(x_stat)
    if abs(x_stat - x_min) < eps:
        print(f"x_min = {x_stat:.{eps_signs}f} f_min = {f_x_stat:.{eps_signs}f}")
        break
    if f_x_stat < f_min:
        x_1 = x_stat
    else:
        x_1 = x_min
