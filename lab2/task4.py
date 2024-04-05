'''
В этой задаче вы реализуете алгоритм бинарного поиска, который позволяет
очень эффективно искать (даже в огромных) списках при условии, что список
отсортирован. Цель - реализация алгоритма двоичного (бинарного) поиска.
• Формат входного файла (input.txt). В первой строке входного файла со-
держится число n (1 ≤ n ≤ 105) — число элементов в массиве, и 
последовательность a0 < a1 < ... < an−1 из n различных положительных целых
чисел в порядке возрастания, 1 ≤ ai ≤ 10^9 для всех 0 ≤ i < n. 
Следующая строка содержит число k, 1 ≤ k ≤ 105 и k положительных целых чисел
b0, ...bk−1, 1 ≤ bj ≤ 10^9 для всех 0 ≤ j < k.
• Формат выходного файла (output.txt). Для всех i от 0 до k − 1 вывести
индекс 0 ≤ j ≤ n − 1, такой что ai = bj или -1, если такого числа в массиве
нет.
• Ограничение по времени. 2сек.
• Ограничение по памяти. 256 мб.
'''

import time
 
t_start = time.perf_counter()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

with open('task4.txt', 'r') as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))
    k = int(file.readline())
    targets = list(map(int, file.readline().split()))

result = []
for i in targets:
    result.append(binary_search(arr, i))

with open('output.txt', 'w') as file:
    for i in result:
        file.write(str(i) + ' ')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
