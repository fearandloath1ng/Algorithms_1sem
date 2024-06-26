'''
«Сортировка пугалом» — это давно забытая народная потешка. Участнику
под верхнюю одежду продевают деревянную палку, так что у него оказываются
растопырены руки, как у огородного пугала. Перед ним ставятся n матрёшек в
ряд. Из-за палки единственное, что он может сделать — это взять в руки две
матрешки на расстоянии k друг от друга (то есть i-ую и i + k-ую), развернуться и
поставить их обратно в ряд, таким образом поменяв их местами.
Задача участника — расположить матрёшки по неубыванию размера. Может
ли он это сделать?
• Формат входного файла (input.txt). В первой строчке содержатся числа
n и k (1 ≤ n, k ≤ 105) – число матрёшек и размах рук. Во второй строчке
содержится n целых чисел, которые по модулю не превосходят 109 – размеры
матрёшек.
• Формат выходного файла (output.txt). Выведите «ДА», если возможно
отсортировать матрёшки по неубыванию размера, и «НЕТ» в противном
случае.
• Ограничение по времени. 2 сек.
• Ограничение по памяти. 256 мб.
'''

import time
 
t_start = time.perf_counter()

def check_sort(arr, k):
    n = len(arr)
    for i in range(n - k):
        if arr[i] > arr[i + k]:
            arr[i], arr[i + k] = arr[i + k], arr[i]
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

with open('task3.txt', 'r') as file:
   n, k = map(int, file.readline().split())
   arr = list(map(int, file.readline().split()))

with open('output.txt', 'w') as file:
   if check_sort(arr, k):
      file.write('ДА')
   else:
      file.write('НЕТ')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))