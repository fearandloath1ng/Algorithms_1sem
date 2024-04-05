'''
Пузырьковая сортировка представляет собой популярный, 
но не очень эффективный алгоритм сортировки. В его основе лежит многократная 
перестановка соседних элементов, нарушающих порядок сортировки. 
Вот псевдокод этой сортировки:

Bubble_Sort(A):
for i = 1 to A.length - 1
for j = A.length downto i+1
if A[j] < A[j-1]
поменять A[j] и A[j-1] местами

Напишите код на Python и докажите корректность пузырьковой сортировки. 
Для доказательства корректоности процедуры вам необходимо доказать, что
она завершается и что A′[1] ≤ A′[2] ≤ ... ≤ A′[n], где A′- выход процедуры
Bubble_Sort, a n - длина массива A.
Определите время пузырьковой сортировки в наихудшем случае и в среднем
случае и сравните его со временем сортировки вставкой.
Формат входного и выходного файла и ограничения - как в задаче 1.
'''

import time
 
t_start = time.perf_counter()

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

    return array

def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        array = list(map(int, file.readline().split()))
    return n, array

def write_output(filename, array):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, array)))

n, array = read_input('task1.txt')
sorted_array = bubble_sort(array)
write_output('output.txt', sorted_array)

print("Время работы: %s секунд " % (time.perf_counter() - t_start))

'''
Доказательство:
Алгоритм завершается, так как внутренний цикл всегда 
уменьшает количество сравнений и обменов.
Также после каждой итерации внешнего цикла наибольший элемент 
будет перемещен в конец массива, поэтому A′[1] ≤ A′[2] ≤ ... ≤ A′[n].
'''