"""Решение задачи коммивояжёра полным перебором"""

# импортируем необходимые библиотеки
from prettytable import PrettyTable

# 3 задачи на выбор:
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


def get_problem():  # пользователь выбирает задачу
    print("Выберите задачу коммивояжёра, которая будет решаться полным перебором:")
    print("Задача №1: 5 городов, симметричная матрица смежности между городами:")
    table_1 = PrettyTable()
    table_1.field_names = ["Город", "1", "2", "3", "4", "5"]
    for i in range(n_1):
        row = [f"{i + 1}"]
        for j in range(n_1):
            row.append(adjacency_matrix_1[i][j] if adjacency_matrix_1[i][j] != None else "-")
        table_1.add_row(row)
    print(table_1)
    print("Задача №2: 5 городов, асимметричная матрица смежности между городами:")
    table_2 = PrettyTable()
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
    table_3 = PrettyTable()
    table_3.field_names = ["Город", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    for i in range(n_3):
        row = [f"{i + 1}"]
        for j in range(n_3):
            row.append(adjacency_matrix_3[i][j] if adjacency_matrix_3[i][j] != None else "-")
        table_3.add_row(row)
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
                    return n_1, adjacency_matrix_1
                elif number_choice == 2:
                    return n_2, adjacency_matrix_2
                else:
                    return n_3, adjacency_matrix_3


def get_start_vertex(n):  # пользователь выбирает стартовую вершину
    while True:
        try:
            number_choice = int(input(f"Введите номер стартовой вершины от 1 до {n}: "))
        except ValueError:
            print("Вы ввели не целое число - введите ещё раз")
        else:
            if number_choice not in (elem for elem in range(1, n + 1)):
                print(f"Вы ввели число, отличное от диапазона от 1 до {n} - введите ещё раз")
            else:
                return number_choice - 1


# решение задачи коммивояжёра полным перебором
def complete_search_ways(n, adjacency_matrix, table, start_v, cur_v, total_dist, total_v, used_v):
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
        return (total_dist + adjacency_matrix[cur_v][start_v], [[start_v, cur_v]], table)
    vars = []
    for v in range(n):
        if (adjacency_matrix[cur_v][v] != None) and (used_v[v] == 0):
            var = complete_search_ways(n, adjacency_matrix, table, start_v, v, total_dist + adjacency_matrix[cur_v][v],
                                       total_v, used_v)
            if var != None:
                vars.append((var[0], var[1]))
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
    return (dist_min, ways_min, table)


def main():  # главная функция программы
    # получаем данные от пользователя
    n, adjacency_matrix = get_problem()
    start_v = get_start_vertex(n)
    # получаем решение задачи коммивояжёра полным перебором
    table = PrettyTable()
    table.field_names = ["Расстояние", "Путь"]
    search_result = complete_search_ways(n, adjacency_matrix, table, start_v, start_v, 0, 0, [0] * n)
    # вывод ответа
    if search_result == None:
        print("Не существует ни одного подходящего пути")
    else:
        dist_min, ways_min, table = search_result
        print("Все возможные пути с возвратом в стартовую вершину:")
        print(table)
        print()
        for i in range(len(ways_min)):
            ways_min[i] = [elem + 1 for elem in ways_min[i]][::-1]  # так как был возвращён обратный путь
        print(f"Минимальное расстояние = {dist_min}")
        print("Оптимальные пути:")
        for way_min in ways_min:
            print(*way_min, sep=" -> ")


main()
input()  # чтобы консоль не закрылась
