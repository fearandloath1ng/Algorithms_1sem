'''
В постфиксной записи (или обратной польской записи) операция записывается
после двух операндов. Например, сумма двух чисел A и B записывается как A B
+. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D
* + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она
не требует скобок и дополнительных соглашений о приоритете операторов для
своего чтения.
Дано выражение в обратной польской записи. Определите его значение.
• Формат входного файла (input.txt). В первой строке входного файла дано
число N (1 ≤ n ≤ 10^6) – число элементов выражения. Во второй строке
содержится выражение в постфиксной записи, состоящее из N элементов. В
выражении могут содержаться неотрицательные однозначные числа и 
операции +, -, *. Каждые два соседних элемента выражения разделены ровно одним пробелом.
• Формат выходного файла (output.txt). Необходимо вывести значение за-
писанного выражения. Гарантируется, что результат выражения, а также
результаты всех промежуточных вычислений, по модулю будут меньше, чем 2^31.
• Ограничение по времени. 2 сек.
• Ограничение по памяти. 256 мб.
'''

import time
 
t_start = time.perf_counter()

def postfix_eval(expression):
    stack = []
    for char in expression:
        if char in '+-*/':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = eval(f'{operand1} {char} {operand2}')
            stack.append(result)
        else:
            stack.append(int(char))
    return stack[0]

with open('task8.txt', 'r') as f:
    n = int(f.readline())
    expression = f.readline().split()
result = postfix_eval(expression)
with open('output.txt', 'w') as f:
    f.write(str(result))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))