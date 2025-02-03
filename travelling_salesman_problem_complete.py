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
# граф №3 - асимметричный из 10 вершин
n_3 = 10
adjacency_matrix_3 = [
    [None, 12, 16, 18, 13, 6, None, 11, 4, 4],
    [2, None, 13, 4, None, 8, 8, 11, 20, 5],
    [None, 3, None, 3, 18, 6, 17, 8, 13, None],
    [None, 6, 11, None, 14, 9, 14, None, 17, 10],
    [5, None, 3, 2, None, 4, 10, 19, None, 20],
    [None, None, 8, None, None, 3, None, 17, None, None],
    [None, None, 20, 9, None, 7, None, 19, 3, 4],
    [None, 16, 9, 17, None, 5, 9, None, 8, 13],
    [None, 13, 16, 3, 2, 4, 6, 10, None, 6],
    [7, None, 17, 4, 7, None, 16, 13, 6, None]
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
    print("Задача №3: 10 городов, асимметричная матрица смежности между городами:")
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
                return number_choice - 1  # так как в матрицах нумерация вершин начинается с 0


def complete_search_of_all_ways(n, adjacency_matrix, start_v, all_ways, cur_v, total_v, total_dist, total_way, used_v):
    # n, adjacency_matrix, start_v - информация, all_ways - ссылка на таблицу всех путей, которая попопляется,
    # cur_v - текущая вершина, total_v - вершин пройдено на данный момент,
    # total_dist - расстояние пройденное на данный момент, total_way - текущий путь на данный момент,
    # used_v - список посещённых вершин
    if total_v == n:
        if adjacency_matrix[cur_v][start_v] != None:
            total_dist += adjacency_matrix[cur_v][start_v]
            total_way += f" -> {start_v + 1}"
            all_ways.append((total_dist, total_way))
    else:
        for next_v in range(n):
            if used_v[next_v] == 0 and adjacency_matrix[cur_v][next_v] != None:
                used_v[next_v] = 1
                complete_search_of_all_ways(n, adjacency_matrix, start_v, all_ways, next_v, total_v + 1, total_dist +
                                     adjacency_matrix[cur_v][next_v], total_way + f" -> {next_v + 1}", used_v)
                used_v[next_v] = 0


def main():  # главная функция программы
    # получаем данные от пользователя
    n, adjacency_matrix = get_problem()
    start_v = get_start_vertex(n)
    # получаем решение задачи коммивояжёра полным перебором
    all_ways = []  # таблица всех возможных путей, в ф-цию передаём ссылку на неё, чтобы она пополнялась
    complete_search_of_all_ways(n, adjacency_matrix, start_v, all_ways, start_v, 1, 0,
                                f"{start_v + 1}", [0 if x != start_v else 1 for x in range(n)])
    # теперь таблица all_ways сформирована, можно обработать её, превратив в красивую таблицу и найти кратчайшие пути
    if len(all_ways) > 0:
        all_ways_prettytable = PrettyTable()
        all_ways_prettytable.field_names = ["Расстояние", "Путь"]
        min_dist, optimal_ways = 100000000000000000000000000000000, []
        for dist, way in all_ways:
            all_ways_prettytable.add_row([dist, way])
            if dist < min_dist:
                min_dist = dist
                optimal_ways = [way]
            elif dist == min_dist:
                optimal_ways.append(way)
        # вывод ответов
        print(all_ways_prettytable)
        print(f"Минимальное расстрояние = {min_dist}")
        print("Оптимальные пути:", *optimal_ways, sep="\n")
    else:
        print("Не существует ни одного подходящего пути")


main()
input()  # чтобы консоль не закрылась
