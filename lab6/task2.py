'''
В этой задаче ваша цель - реализовать простой менеджер телефонной книги.
Он должен уметь обрабатывать следующие типы пользовательских запросов:
• add number name – это команда означает, что пользователь добавляет в
телефонную книгу человека с именем name и номером телефона number.
Если пользователь с таким номером уже существует, то ваш менеджер 
должен перезаписать соответствующее имя.
• del number – означает, что менеджер должен удалить человека с номером 
из телефонной книги. Если такого человека нет, то он должен просто
игнорировать запрос.
• find number – означает, что пользователь ищет человека с номером 
телефона number. Менеджер должен ответить соответствующим именем или
строкой «not found» (без кавычек), если такого человека в книге нет.
• Формат ввода / входного файла (input.txt). В первой строке входного
файла содержится число N (1 ≤ N ≤ 10^5) - количество запросов. Далее
следуют N строк, каждая из которых содержит один запрос в формате, описанном выше.
Все номера телефонов состоят из десятичных цифр, в них нет нулей в начале
номера, и каждый состоит не более чем из 7 цифр. Все имена представляют
собой непустые строки из латинских букв, каждая из которых имеет длину
не более 15. Гарантируется при проверке, что не будет человека с именем
«not found».
• Формат вывода / выходного файла (output.txt). Выведите результат 
каждого поискового запроса find – имя, соответствующее номеру телефона,
или «not found» (без кавычек), если в телефонной книге нет человека с 
таким номером телефона. Выведите по одному результату в каждой строке в
том же порядке, как были заданы запросы типа find во входных данных.
• Ограничение по времени. 6 сек.
• Ограничение по памяти. 512 мб.
'''

import time
 
t_start = time.perf_counter()

class PhoneBookManager:
    def __init__(self):
        self.phone_book = {}

    def add_contact(self, number, name):
        self.phone_book[number] = name

    def del_contact(self, number):
        if number in self.phone_book:
            del self.phone_book[number]

    def find_contact(self, number):
        if number in self.phone_book:
            return self.phone_book[number]
        else:
            return "not found"

    def process_queries(self, queries):
        results = []
        for query in queries:
            query_parts = query.split()
            command = query_parts[0]
            number = query_parts[1]
            if command == "add":
                name = query_parts[2]
                self.add_contact(number, name)
            elif command == "del":
                self.del_contact(number)
            elif command == "find":
                result = self.find_contact(number)
                results.append(result)
        return results

with open("task2.txt", "r") as file:
    n = int(file.readline())
    queries = [file.readline().strip() for _ in range(n)]

manager = PhoneBookManager()
results = manager.process_queries(queries)

with open("output.txt", "w") as file:
    for result in results:
        file.write(result + "\n")

print("Время работы: %s секунд " % (time.perf_counter() - t_start))