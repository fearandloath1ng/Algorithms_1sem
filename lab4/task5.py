'''
Стек - это абстрактный тип данных, поддерживающий операции Push() и
Pop(). Нетрудно реализовать его таким образом, чтобы обе эти операции работали
за константное время. В этой задаче ваша цель - реализовать стек, который также
поддерживает поиск максимального значения и гарантирует, что все операции
по-прежнему работают за константное время.
Реализуйте стек, поддерживающий операции Push(), Pop() и Max().
• Формат входного файла (input.txt). В первой строке входного файла со-
держится n (1 ≤ n ≤ 400000) – число команд. Последющие n строк исходно-
го файла содержит ровно одну команду: push V, pop или max. 0 ≤ V ≤ 10^5.
• Формат выходного файла (output.txt). Для каждого запроса max выведите
(в отдельной строке) максимальное значение стека.
• Ограничение по времени. 5 сек.
• Ограничение по памяти. 512 мб.
'''

import time
 
t_start = time.perf_counter()

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]

with open('task5.txt', 'r') as file:
    n = int(file.readline().strip())
    commands = [file.readline().strip() for _ in range(n)]

max_stack = MaxStack()
result = []
for command in commands:
    if command.startswith('push'):
        value = int(command.split()[1])
        max_stack.push(value)
    elif command == 'pop':
        max_stack.pop()
    elif command == 'max':
        result.append(max_stack.max())

with open('output.txt', 'w') as file:
    for max_value in result:
        file.write(str(max_value) + '\n')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))