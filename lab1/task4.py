'''
Рассмотрим задачу поиска.
Формат входного файла. Последовательность изn чисел A = a1, a2, . . . , an
в первой строке, числа разделены пробелом, и значение V во второй строке.
Ограничения: 0 ≤ n ≤ 103, −103 ≤ ai, V ≤ 103
Формат выходного файла. Одно число - индекс i, такой, что V = A[i],
или значение −1, если V в отсутствует.
Напишите код линейного поиска, при работе которого выполняется скани-
рование последовательности в поисках значения V .
Если число встречается несколько раз, то выведите, сколько раз встречается
число и все индексы i через запятую.
Дополнительно: попробуйте найти свинью, как в лекции. Используйте во
входном файле последовательность слов из лекции, и найдите соответству-
ющий индекс.
'''

def linear_search(sequence, value):
    indices = []
    for i in range(len(sequence)):
        if sequence[i] == value:
            indices.append(i)
    if indices:
        return len(indices), indices
    else:
        return -1

sequence = list(map(int, input().split()))
value = int(input())

result = linear_search(sequence, value)

if result != -1 and len(result[1]) > 1:
    print(int(result[0]))
    print(*[index + 1 for index in result[1]], sep=', ')
elif result != -1 and len(result[1]) == 1:
    print(*[index + 1 for index in result[1]], sep=', ')
else:
    print(-1)