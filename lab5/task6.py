'''
Реализуйте очередь с приоритетами. Ваша очередь должна поддерживать сле-
дующие операции: добавить элемент, извлечь минимальный элемент, уменьшить
элемент, добавленный во время одной из операций.
• Формат входного файла (input.txt). В первой строке входного файла 
содержится число n (1 ≤ n ≤ 10^6) - число операций с очередью.
Следующие n строк содержат описание операций с очередью, по одному
описанию в строке. Операции могут быть следующими:
– A x – требуется добавить элемент x в очередь.
– X – требуется удалить из очереди минимальный элемент и вывести
его в выходной файл. Если очередь пуста, в выходной файл требуется
вывести звездочку «*».
– D x y – требуется заменить значение элемента, добавленного в очередь
операцией A в строке входного файла номер x + 1, на y. 
Гарантируется, что в строке x + 1 действительно находится операция A, что
этот элемент не был ранее удален операцией X, и что y меньше, чем
предыдущее значение этого элемента.
В очередь помещаются и извлекаются только целые числа, не превышающие
по модулю 10^9.
• Формат выходного файла (output.txt). Выведите последовательно 
результат выполнения всех операций X, по одному в каждой строке выходного
файла. Если перед очередной операцией X очередь пуста, выведите вместо
числа звездочку «*».
• Ограничение по времени. 2 сек.
• Ограничение по памяти. 256 мб.
'''

import time
 
t_start = time.perf_counter()

class PriorityQueue:
    def __init__(self):
        self.a = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def min_heapify(self, i):
        lowest = i
        l = self.left_child(i)
        r = self.right_child(i)
        
        if l < len(self.a) and self.a[l][0] < self.a[lowest][0]:
            lowest = l
        if r < len(self.a) and self.a[r][0] < self.a[lowest][0]:
            lowest = r
        
        if lowest != i:
            self.a[i], self.a[lowest] = self.a[lowest], self.a[i]
            self.min_heapify(lowest)
    
    def decrease_key(self, i, key):
        self.a[i] = (key, self.a[i][1])
        while i > 0 and self.a[i][0] < self.a[self.parent(i)][0]:
            self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
            i = self.parent(i)
    
    def index_searching(self, x, key):
        for i in range(len(self.a)):
            if self.a[i][1] == x:
                self.decrease_key(i, key)
                break
    
    def insert(self, key, n_line):
        self.a.append((float('inf'), n_line))
        self.decrease_key(len(self.a) - 1, key)
    
    def extract_min(self):
        if not self.a:
            return '*'
        
        current_min = self.a[0][0]
        self.a[0] = self.a[-1]
        self.a.pop()
        self.min_heapify(0)
        
        return current_min
    
    def processing(self):
        with open("task6.txt", "r") as file_in, open("output.txt", "w") as file_out:
            n = int(file_in.readline().strip())
            
            for _ in range(n):
                line = file_in.readline().strip().split()
                if line[0] == 'A':
                    x = int(line[1])
                    self.insert(x, _ + 1)
                elif line[0] == 'X':
                    result = self.extract_min()
                    file_out.write(str(result) + '\n')
                elif line[0] == 'D':
                    x = int(line[1])
                    y = int(line[2])
                    self.index_searching(x, y)

queue = PriorityQueue()
queue.processing()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))