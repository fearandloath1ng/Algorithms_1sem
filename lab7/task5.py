'''
Вычислить длину самой длинной общей подпоследовательности из трех последовательностей.
Даны три последовательности A = (a[1], a[2], ..., a[n]), B = (b[1], b[2], ..., b[m]) и 
C = (c[1], c[2], ..., c[l]), найти длину их самой длинной общей подпоследовательности, т.е.
наибольшее неотрицатеьное целое число p такое, что существуют индексы 
1 ≤ i[1] < i[2] < ... < i[p] ≤ n, 1 ≤ j[1] < j[2] < ... < j[p] ≤ m и 1 ≤ k[1] < k[2] < ... < k[p] ≤ l
такие, что a[i[1]] = b[j[1]] = c[k[1]], ..., a[i[p]] = b[j[p]] = c[k[p]].
• Формат ввода / входного файла (input.txt).
– Первая строка: n - длина первой последовательности.
– Вторая строка: a[1], a[2], ..., a[n] через пробел.
– Третья строка: m - длина второй последовательности.
– Четвертая строка: b[1], b[2], ..., b[m] через пробел.
– Пятая строка: l - длина второй последовательности.
– Шестая строка: c[1], c[2], ..., c[l] через пробел.
• Ограничения: 1 ≤ n, m, l ≤ 100; −10^9 < a[i], b[i], c[i] < 10^9.
• Формат вывода / выходного файла (output.txt). Выведите число p.
• Ограничение по времени. 1 сек.
'''

import time
 
t_start = time.perf_counter()

def longest_common_subsequence(A, B, C):
    n, m, l = len(A), len(B), len(C)
    dp = [[[0 for _ in range(l+1)] for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                if A[i-1] == B[j-1] == C[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    return dp[n][m][l]

with open("task5.txt", "r") as file:
    n = int(file.readline())
    A = list(map(int, file.readline().split()))
    m = int(file.readline())
    B = list(map(int, file.readline().split()))
    l = int(file.readline())
    C = list(map(int, file.readline().split()))

result = longest_common_subsequence(A, B, C)
with open("output.txt", "w") as file:
    file.write(str(result))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))