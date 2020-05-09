from numpy import inf as INF  # с пакета numpy импортируем константу - бесконечность

def floyds_algorithm(weighing_matrix, show=False):
    """
    Реализация алгоритма Флойда для решения задачи поиска кратчайших путей
    между всеми парами вершин взвешенного связного графа

    Parameters
    ----------
    weighing_matrix: весовая матрица
    show: {True, False}, default 'False'
        * True: выведет результат выполнения функции на экран
        * False: вернет объект выполнения функции

    Returns
    -------
    Матрица кратчайших путей между всеми парами вершин взвешенного связного графа
    """

    from copy import deepcopy  # импортируем функцию глубокого копирования
    # для структур с вложеность больше 1

    n = len(weighing_matrix)  # вычисляем порядок матрица
    A = deepcopy(weighing_matrix)  # инициализируем матрицу кратчайших путей

    # алгоритм Флойда
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])

    # вывод на экран или возвращение матрицы кратчайших путей
    if show:
        display_matrix(A, title='Матрица расстояний:\n')
    else:
        return A


def display_matrix(matrix, title=False):
    """
    Вывод матрицы на экран в удобном виде

    Parameters
    ----------
    matrix: матрица
    title: {False, str}, default 'False'
        * False: без названия
        * str: название матрицы

    """

    # Если есть название, выводим его
    if title:
        print(title)

    for raw, _ in enumerate(matrix):  # итерируемся по строкам матрицы
        print(*matrix[raw], sep='\t')  # выводим распаковавную строку, с таб-разделителем

    print('\n')  # делаем 2 отступа в конце


# Инициализируем весовую матрицу
W = [
    [0, 8, 5],
    [3, 0, INF],
    [INF, 2, 0],
]

# Выводим весовую матрицу на экран
display_matrix(W, title='Весовая матрица:')

# Находим и выводим матрицу кратчайших путей на экран
floyds_algorithm(W, show=True)
