'''
Как известно, в США президент выбирается не прямым голосованием, а путем
двухуровневого голосования. Сначала проводятся выборы в каждом штате и 
определяется победитель выборов в данном штате. Затем проводятся государственные
выборы: на этих выборах каждый штат имеет определенное число голосов — число 
выборщиков от этого штата. На практике, все выборщики от штата голосуют
в соответствии с результами голосования внутри штата, то есть на заключительной 
стадии выборов в голосовании участвуют штаты, имеющие различное число
голосов. Вам известно за кого проголосовал каждый штат и сколько голосов 
было отдано данным штатом. Подведите итоги выборов: для каждого из участника
голосования определите число отданных за него голосов.
• Формат ввода / входного файла (input.txt).Каждая строка входного файла
содержит фамилию кандидата, за которого отдают голоса выборщики этого
штата, затем через пробел идет количество выборщиков, отдавших голоса
за этого кандидата.
• Формат вывода / выходного файла (output.txt). Выведите фамилии всех
кандидатов в лексикографическом порядке, затем, через пробел, 
количество отданных за них голосов.
• Ограничение по времени. 2 сек.
• Ограничение по памяти. 64 мб.
'''

import time
 
t_start = time.perf_counter()

def election_results():
    with open('task5.txt', 'r') as file:
        data = file.readlines()

    results = {}

    for line in data:
        candidate, votes = line.strip().split(' ')
        votes = int(votes)

        if candidate not in results:
            results[candidate] = votes
        else:
            results[candidate] += votes

    candidates = sorted(results.keys())

    with open('output.txt', 'w') as file:
        for candidate in candidates:
            file.write(f"{candidate} {results[candidate]}\n")

election_results()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))