# Метод Пауэлла
# ЗДЕСЬ ТОЧНОСТЬ МИНИМАЛЬНАЯ EPS = 10^-13 из-за Decimal
import math
import decimal
from decimal import Decimal
def f(x):  # входная функция № 1
    return ((x + Decimal("1")) * (x + Decimal("4")) ** Decimal("3"))
# def f(x):  # входная функция № 2
#     return (x ** Decimal("2") - Decimal(str(math.sin(x))))
# def f(x):  # входная функция № 3
#     return (x ** Decimal("4") + Decimal("8") * x ** Decimal("3") - Decimal("6") * x ** Decimal("2")
#             - Decimal("72") * x + Decimal("90"))


a, b = Decimal("-2"), Decimal("-1")  # входные данные № 1
# a, b = Decimal("0"), Decimal(str(math.pi)) / Decimal("2")  # входные данные № 2
# a, b = Decimal("1.5"), Decimal("2")  # входная функция № 3

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
