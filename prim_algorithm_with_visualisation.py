"""
Алгоритм Прима для нахождения минимального остова графа. Минимальное остовное дерево (минимальный остов) - это
такое поддерево этого графа, которое соединяет все его вершины, и при этом обладает наименьшим возможным весом
 (т.е. суммой весов рёбер). Если остовных деревьев несколько - выбираем любое. Реализован тривиальный алгоритм Прима.
"""

import math
import prettytable
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

def prim_algorithm():
    global n, m, edge_list
    used_v, edges = [0] * n, []
    used_v[0] = 1
    total_v, total_w = 1, 0
    for i in range(n - 1):
        w_min, v_add, edge_add = 10000000000000000000000000000000, None, None
        for j in range(m):
            edge = edge_list[j]
            v_1, v_2, w = edge
            if (used_v[v_1] + used_v[v_2]) == 1:
                if w < w_min:
                    w_min = w
                    v_add = v_1 if used_v[v_1] == 0 else v_2
                    edge_add = edge
        used_v[v_add] = 1
        edges.append(edge_add)
        total_v += 1
        total_w += w_min
    return total_w, edges


def draw_graph_answer(n, m, all_edges, chosen_edges):
    # рисует граф для любого кол-ва вершин, располагая их на единичной тригонометрической окружности
    # создание фигуры, на к-рой будут размещаться графики (в нашем случае - один график)
    fig = plt.figure(figsize=(6, 6))
    p = fig.add_subplot()
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    v_coords = []
    fi = (2 * math.pi) / n
    total_fi = 0
    for i in range(n):
        total_fi += fi
        if total_fi in (0, math.pi / 2, math.pi, (3 * math.pi) / 2, 2 * math.pi):
            if total_fi == 0:
                x, y = 1, 0
            elif total_fi == (math.pi / 2):
                x, y = 0, 1
            elif total_fi == math.pi:
                x, y = -1, 0
            elif total_fi == ((3 * math.pi) / 2):
                x, y = 0, -1
            else:
                x, y = 1, 0
        elif 0 < total_fi < (math.pi / 2):
            x, y = math.cos(total_fi), math.sin(total_fi)
        elif (math.pi / 2) < total_fi < math.pi:
            x, y = -math.cos(math.pi - total_fi), math.sin(math.pi - total_fi)
        elif math.pi < total_fi < ((3 * math.pi) / 2):
            x, y = -math.cos(total_fi - math.pi), -math.sin(total_fi - math.pi)
        else:
            x, y = math.cos((2 * math.pi) - total_fi), -math.sin((2 * math.pi) - total_fi)
        p.scatter([x], [y], marker="o", color="orange")
        p.text(x + 0.1, y, f"{i + 1}", fontweight='bold')
        v_coords.append((x, y))
    for edge in all_edges:
        v_1, v_2, w = edge
        if edge in chosen_edges:
            edge_color = "orange"
        else:
            edge_color = "grey"
        p.plot([v_coords[v_1][0], v_coords[v_2][0]], [v_coords[v_1][1], v_coords[v_2][1]], color=edge_color)
        x_mid, y_mid = (v_coords[v_1][0] + v_coords[v_2][0]) / 2, (v_coords[v_1][1] + v_coords[v_2][1]) / 2
        p.text(x_mid, y_mid, w, color=edge_color)
    plt.axis("off")  # скрытие осей
    plt.show()  # вывод графика


# 3 задачи на выбор
# граф №1 - 5 вершин графа, 7 рёбер
n_1, m_1 = 5, 7
# список рёбер в формате (вершина №1, вершина №2, вес ребра) без повторений, т. к. граф неориентированный
edge_list_1 = [
    (0, 1, 3), (0, 2, 4), (0, 4, 1), (1, 2, 5), (2, 3, 2), (2, 4, 6), (3, 4, 7)
]
# граф №2 - 7 вершин графа, 11 рёбер
n_2, m_2 = 7, 11
edge_list_2 = [
    (0, 1, 7), (0, 3, 5), (1, 2, 8), (1, 3, 9), (1, 4, 7), (2, 4, 5), (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9),
    (5, 6, 11)
]
# граф №3 - 10 вершин графа, 21 рёбер
n_3, m_3 = 10, 21
edge_list_3 = [
    (0, 1, 6), (0, 2, 3), (0, 4, 9), (1, 2, 4), (1, 3, 2), (1, 6, 9), (2, 3, 2), (2, 4, 9), (2, 5, 9), (3, 5, 8),
    (3, 6, 9), (4, 5, 8), (4, 9, 18), (5, 6, 7), (5, 8, 9), (5, 9, 10), (6, 7, 4), (6, 8, 5), (7, 8, 1), (7, 9, 4),
    (8, 9, 3)
]

# пользователь выбирает задачу
print("Выберите задачу, для которой будет искаться минимальный остов алгоритмом Прима:")
print("Задача №1: список рёбер для неориентированного связного графа из 5 вершин:")
table_1 = prettytable.PrettyTable()
table_1.field_names = ["Ребро №", "Вершина A", "Вершина B", "Вес ребра между A и B"]
for i in range(m_1):
    table_1.add_row([i + 1, edge_list_1[i][0] + 1, edge_list_1[i][1] + 1, edge_list_1[i][2]])
print(table_1)
print("Задача №2: список рёбер для неориентированного связного графа из 7 вершин:")
table_2 = prettytable.PrettyTable()
table_2.field_names = ["Ребро №", "Вершина A", "Вершина B", "Вес ребра между A и B"]
for i in range(m_2):
    table_2.add_row([i + 1, edge_list_2[i][0] + 1, edge_list_2[i][1] + 1, edge_list_2[i][2]])
print(table_2)
print("Задача №3: список рёбер для неориентированного связного графа из 10 вершин:")
table_3 = prettytable.PrettyTable()
table_3.field_names = ["Ребро №", "Вершина A", "Вершина B", "Вес ребра между A и B"]
for i in range(m_3):
    table_3.add_row([i + 1, edge_list_3[i][0] + 1, edge_list_3[i][1] + 1, edge_list_3[i][2]])
print(table_3)
while True:
    try:
        number_choice = int(input("Введите число 1, 2 или 3: "))
    except ValueError:
        print("Вы ввели не целое число - введите ещё раз")
    else:
        if number_choice not in (1, 2, 3):
            print("Вы ввели число, отличное от 1, 2 или 3 - введите ещё раз")
        else:
            if number_choice == 1:
                n, m, edge_list = n_1, m_1, edge_list_1
                print("Решаемая задача: список рёбер для неориентированного связного графа из 5 вершин:")
                print(table_1)
            elif number_choice == 2:
                n, m, edge_list = n_2, m_2, edge_list_2
                print("Решаемая задача: список рёбер для неориентированного связного графа из 7 вершин:")
                print(table_2)
            else:
                n, m, edge_list = n_3, m_3, edge_list_3
                print("Решаемая задача: список рёбер для неориентированного связного графа из 10 вершин:")
                print(table_3)
            break
print()

total_w_min, edges_min = prim_algorithm()
table = prettytable.PrettyTable()
table.field_names = ["Вершина A", "Вершина B", "Вес ребра между A и B"]
for edge in edges_min:
    table.add_row([edge[0] + 1, edge[1] + 1, edge[2]])
print(f"Вес минимального остовного дерева = {total_w_min}")
print("Рёбра графа, входящие в остов:")
print(table)
draw_graph_answer(n, m, edge_list, edges_min)
input()  # чтобы консоль не закрылась
