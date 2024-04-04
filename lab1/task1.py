'''
Используя код процедуры Insertion-sort, напишите программу и проверьте сор-
тировку массива A = {31, 41, 59, 26, 41, 58}.
Формат входного файла (input.txt). В первой строке входного файла со-
держится число n (1 ≤ n ≤ 103) — число элементов в массиве. Во второй
строке находятся n различных целых чисел, по модулю не превосходящих
109.
Формат выходного файла (output.txt). Одна строка выходного файла с
отсортированным массивом. Между любыми двумя числами должен стоять
ровно один пробел.
Ограничение по времени. 2сек.
Ограничение по памяти. 256 мб.
Выберите любой набор данных, подходящих по формату, и протестируйте
алгоритм.
'''

from typing import List, NoReturn, Union
import time
 
t_start = time.perf_counter()

def insertion_sort(array: List[Union[int, float]]) -> NoReturn:
    length = len(array)
    for i in range(1, length):
        tmp = array[i]
        j = i - 1
        while j >= 0 and array[j] > tmp:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp

with open('task1.txt', 'r') as file:
  lines = file.readlines()
  length = [int(num) for num in lines[0].split()]
  array = [int(num) for num in lines[1].split()]
insertion_sort(array)
print(*array, sep=' ')
print("Время работы: %s секунд " % (time.perf_counter() - t_start))