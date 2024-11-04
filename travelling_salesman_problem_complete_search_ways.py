"""
Решение задачи коммивояжёра полным перебором - это точный метод, который применяется для небольшого количества городов.
Классическая формулировка задачи коммивояжёра: найти самый короткий маршрут, проходящий через все города по 1 разу с
возвратом в город, с которого начали (то есть в стартовом городе побываем 2 раза), если таких несколько - вывести все.
"""

import prettytable


def complete_search_ways(start_v, cur_v, total_dist, total_v, used_v):
    global n, adjacency_matrix, table
    total_v += 1
    used_v[cur_v] = total_v
    if total_v == n:
        if adjacency_matrix[cur_v][start_v] == None:
            return None
        way = [0] * (n + 1)
        for ind in range(n):
            way[used_v[ind] - 1] = ind + 1
        way[n] = start_v + 1
        way_str = " -> ".join([str(elem) for elem in way])
        table.add_row([total_dist + adjacency_matrix[cur_v][start_v], way_str])
        total_v -= 1
        used_v[cur_v] = 0
        return ((total_dist + adjacency_matrix[cur_v][start_v]), [[start_v, cur_v]])
    vars = []
    for v in range(n):
        if (adjacency_matrix[cur_v][v] != None) and (used_v[v] == 0):
            var = complete_search_ways(start_v, v, total_dist + adjacency_matrix[cur_v][v], total_v, used_v)
            if var != None:
                vars.append(var)
    total_v -= 1
    used_v[cur_v] = 0
    if len(vars) == 0:
        return None
    dist_min, ways_min = 100000000000000000000000000000000000000, None
    for dist, ways in vars:
        if dist < dist_min:
            dist_min = dist
            ways_min = ways
        elif dist == dist_min:
            ways_min.extend(ways)
    for i in range(len(ways_min)):
        ways_min[i].append(cur_v)
    return (dist_min, ways_min)

# 3 задачи на выбор
# граф №1 - симметричный из 5 вершин
n_1 = 5
adjacency_matrix_1 = [
    [None, 5, 6, 14, 15],
    [5, None, 7, 10, 6],
    [6, 7, None, 8, 7],
    [14, 10, 8, None, 9],
    [15, 6, 7, 9, None]
]
# граф №2 - асимметричный из 5 вершин
n_2 = 5
adjacency_matrix_2 = [
    [None, 25, 40, 31, 27],
    [5, None, 17, 30, 25],
    [19, 15, None, 6, 1],
    [9, 50, 24, None, 6],
    [22, 8, 7, 10, None]
]
# граф №3 - асимметричный из 10 вершин, не для всех вершин существует хотя бы 1 путь с возвратом в эту вершину
n_3 = 10
adjacency_matrix_3 = [
    [None, 12, 16, 18, 13, 6, None, 11, 4, 4],
    [2, None, 13, 4, None, 8, 8, 11, 20, 5],
    [None, 3, None, 3, 18, 6, 17, 8, 13, None],
    [4, 6, 11, None, 14, 9, 14, None, 17, 10],
    [13, None, 3, 2, None, 4, 10, 19, None, 20],
    [18, 10, 5, 18, 19, None, 5, 17, 14, 8],
    [5, None, 20, 9, None, 7, None, 19, 3, 4],
    [8, 16, 9, 17, None, 5, 9, None, 8, 13],
    [13, 13, 16, 3, 2, 4, 6, 10, None, 6],
    [20, None, 17, 4, 7, None, 16, 13, 6, None]
]

# пользователь выбирает задачу
print("Выберите задачу коммивояжёра, которая будет решаться полным перебором:")
print("Задача №1: 5 городов, симметричная матрица смежности между городами:")
table_1 = prettytable.PrettyTable()
table_1.field_names = ["Город", "1", "2", "3", "4", "5"]
for i in range(n_1):
    row = [f"{i + 1}"]
    for j in range(n_1):
        row.append(adjacency_matrix_1[i][j] if adjacency_matrix_1[i][j] != None else "-")
    table_1.add_row(row)
print(table_1)
print("Задача №2: 5 городов, асимметричная матрица смежности между городами:")
table_2 = prettytable.PrettyTable()
table_2.field_names = ["Город", "1", "2", "3", "4", "5"]
for i in range(n_2):
    row = [f"{i + 1}"]
    for j in range(n_2):
        row.append(adjacency_matrix_2[i][j] if adjacency_matrix_2[i][j] != None else "-")
    table_2.add_row(row)
print(table_2)
print("Задача №3: 10 городов,",
      "не для всех городов существует хотя бы 1 путь с возвратом в этот город,",
      "асимметричная матрица смежности между городами:", sep="\n")
table_3 = prettytable.PrettyTable()
table_3.field_names = ["Город", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
for i in range(n_3):
    row = [f"{i + 1}"]
    for j in range(n_3):
        row.append(adjacency_matrix_3[i][j] if adjacency_matrix_3[i][j] != None else "-")
    table_3.add_row(row)
print(table_3)
while True:
    try:
        number_choice_1 = int(input("Введите число 1, 2 или 3: "))
    except ValueError:
        print("Вы ввели не целое число - введите ещё раз")
    else:
        if number_choice_1 not in (1, 2, 3):
            print("Вы ввели число, отличное от 1, 2 или 3 - введите ещё раз")
        else:
            if number_choice_1 == 1:
                n, adjacency_matrix = n_1, adjacency_matrix_1
                print("Решаемая задача: 5 городов, симметричная матрица смежности между городами:")
                print(table_1)
            elif number_choice_1 == 2:
                n, adjacency_matrix = n_2, adjacency_matrix_2
                print("Решаемая задача: 5 городов, асимметричная матрица смежности между городами:")
                print(table_2)
            else:
                n, adjacency_matrix = n_3, adjacency_matrix_3
                print("Решаемая задача: 10 городов,",
                      "не для всех городов существует хотя бы 1 путь с возвратом в этот город,",
                      "асимметричная матрица смежности между городами:", sep="\n")
                print(table_3)
            break
print()

# пользователь выбирает стартовую вершину
while True:
    try:
        number_choice_2 = int(input(f"Введите номер стартовой вершины от 1 до {n}: "))
    except ValueError:
        print("Вы ввели не целое число - введите ещё раз")
    else:
        if number_choice_2 not in (elem for elem in range(1, n + 1)):
            print(f"Вы ввели число, отличное от диапазона от 1 до {n} - введите ещё раз")
        else:
            start_v = number_choice_2 - 1
            break
print()

# решение задачи коммивояжёра полным перебором
table = prettytable.PrettyTable()
table.field_names = ["Расстояние", "Путь"]
search_result = complete_search_ways(start_v, start_v, 0, 0, [0] * n)
if search_result == None:
    print("Не существует ни одного подходящего пути")
else:
    print("Все возможные пути с возвратом в стартовую вершину:")
    print(table)
    print()
    dist_min, ways_min = search_result
    for i in range(len(ways_min)):
        ways_min[i] = [elem + 1 for elem in ways_min[i]][::-1]  # так как был возвращён обратный путь
    print(f"Минимальное расстояние = {dist_min}")
    print("Оптимальные пути:")
    for way_min in ways_min:
        print(*way_min, sep=" -> ")
