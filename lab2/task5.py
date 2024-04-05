'''
Правило большинства - это когда выбирается элемент, имеющий больше 
половины голосов. Допустим, есть последовательность A элементов a1, a2, ...an, и
нужно проверить, содержит ли она элемент, который появляется больше, чем n/2
раз. Наивный метод это сделать:

Majority(A):
for i from 1 to n:
current_element = a[i]
count = 0
for j from 1 to n:
if a[j] = current_element:
count = count+1

if count > n/2:
return a[i]
return "нет элемента большинства"

Очевидно, время выполнения этого алгоритма квадратично. 
Ваша цель - использовать метод "Разделяй и властвуй" 
для разработки алгоритма проверки, содержится ли во входной последовательности элемент,
который встречается больше половины раз, за время O(n log n).
• Формат входного файла (input.txt). В первой строке входного файла 
содержится число n (1 ≤ n ≤ 105) — число элементов в массиве. Во второй
строке находятся n положительных целых чисел, по модулю не превосходя-
щих 109, 0 ≤ ai ≤ 109.
• Формат выходного файла (output.txt). Выведите 1, если во входной последовательности
есть элемент, который встречается строго больше половины раз; 
в противном случае - 0.
• Ограничение по времени. 2сек.
• Ограничение по памяти. 256 мб.
'''

import time
 
t_start = time.perf_counter()

def count_majority_element(arr, left, right, candidate):
    count = 0
    for i in range(left, right+1):
        if arr[i] == candidate:
            count += 1
    return count

def find_majority_element(arr, left, right):
    if left == right:
        return arr[left]
    
    mid = (left + right) // 2
    left_majority = find_majority_element(arr, left, mid)
    right_majority = find_majority_element(arr, mid+1, right)
    
    if left_majority == right_majority:
        return left_majority
    
    left_count = count_majority_element(arr, left, right, left_majority)
    right_count = count_majority_element(arr, left, right, right_majority)
    
    if left_count > (right - left + 1) // 2:
        return left_majority
    elif right_count > (right - left + 1) // 2:
        return right_majority
    else:
        return "no such element"

with open("task5.txt", "r") as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))

result = find_majority_element(arr, 0, n-1)

if result != "no such element":
    with open("output.txt", "w") as file:
        file.write("1")
else:
    with open("output.txt", "w") as file:
        file.write("0")

print("Время работы: %s секунд " % (time.perf_counter() - t_start))