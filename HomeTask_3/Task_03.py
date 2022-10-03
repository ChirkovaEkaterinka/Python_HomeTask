# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = [round(random.uniform(0, 10), 2)
           for _ in range(int(input('Введите кол-во элементов списка: ')))]
print('Сгенерируемый список: ', my_list)
new_list_dec = []
for pos in range(0, len(my_list)):
    new_list_dec.append(round((my_list[pos] % 1), 2))
print('Разница между макс и мин знаечнием дробной части: ', max(new_list_dec)-min(new_list_dec))
