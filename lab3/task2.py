'''
Для сортировки последовательности чисел широко используется быстрая сор-
тировка - QuickSort. Далее приведена программа на языке Pascal Python, которая
сортирует массив a, используя этот алгоритм.

def qsort (left, right):
key = a [(left + right) // 2]
i = left
j = right
while i <= j:
while a[i] < key: # first while
i += 1
while a[j] > key : # second while
j -= 1
if i <= j :
a[i], a[j] = a[j], a[i]
i += 1
j -= 1

if left < j:
qsort(left, j)
if i < right:
qsort(i, right)

qsort(0, n - 1)

Хотя QuickSort является очень быстрой сортировкой в среднем, существуют те-
сты, на которых она работает очень долго. Оценивать время работы алгоритма
будем числом сравнений с элементами массива (то есть, суммарным числом срав-
нений в первом и втором while). Требуется написать программу, генерирующую
тест, на котором быстрая сортировка сделает наибольшее число таких сравнений.
Задача на acmp.
• Формат входного файла (input.txt). В первой строке находится единствен-
ное число n (1 ≤ n ≤ 106).
• Формат выходного файла (output.txt). Вывести перестановку чисел от 1 до
n, на которой быстрая сортировка выполнит максимальное число сравнений.
Если таких перестановок несколько, вывести любую из них.
• Ограничение по времени. 2 сек.
• Ограничение по памяти. 256 мб.
'''

import time
 
t_start = time.perf_counter()

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def antiQuickSortPermutation(n):
    perm = list(range(1, n + 1))

    for i in range(2, n):
        swap(perm, i // 2, i)

    return perm

def main():
    with open('task2.txt', 'r') as f:
        n = int(f.read())

    perm = antiQuickSortPermutation(n)

    with open('output.txt', 'w') as f:
        for x in perm:
            f.write(f"{x} ")
        f.write('\n')

if __name__ == "__main__":
    main()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))