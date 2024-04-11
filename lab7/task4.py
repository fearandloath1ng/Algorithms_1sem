'''
Вычислить длину самой длинной общей подпоследовательности из двух последовательностей.
Даны две последовательности A = (a[1], a[2], ..., a[n]) и B = (b[1], b[2], ..., b[m]), найти
длину их самой длинной общей подпоследовательности, т.е. наибольшее неотрицательное 
целое число p такое, что существуют индексы 1 ≤ i[1] < i[2] < ... < i[p] ≤ n
и 1 ≤ j[1] < j[2] < ... < j[p] ≤ m такие, что a[i[1]] = b[j[1]], ..., a[i[p]] = b[j[p]].
• Формат ввода / входного файла (input.txt).
– Первая строка: n - длина первой последовательности.
– Вторая строка: a[1], a[2], ..., a[n] через пробел.
– Третья строка: m - длина второй последовательности.
– Четвертая строка: b[1], b[2], ..., b[m] через пробел.
• Ограничения: 1 ≤ n, m ≤ 100; −10^9 < a[i], b[i] < 10^9.
• Формат вывода / выходного файла (output.txt). Выведите число p.
• Ограничение по времени. 1 сек.
'''

import time
 
t_start = time.perf_counter()

def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

with open('task4.txt', 'r') as file:
    n = int(file.readline())
    A = list(map(int, file.readline().split()))
    m = int(file.readline())
    B = list(map(int, file.readline().split()))

p = longest_common_subsequence(A, B)

with open('output.txt', 'w') as file:
    file.write(str(p))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))