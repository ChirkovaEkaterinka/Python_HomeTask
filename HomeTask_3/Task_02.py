# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

my_list = [random.randint(-10, 10)
           for _ in range(int(input('Введите кол-во элементов списка: ')))]
print('Сгенерируемый список: ', my_list)
new_list = []
if len(my_list) % 2 == 0:
    for pos in range(0, round(len(my_list)/2)):
        new_list.append(my_list[pos]*my_list[len(my_list)-pos-1])
if len(my_list) % 2 == 1:
    for pos in range(0, ((len(my_list)//2)+1)):
        new_list.append(my_list[pos]*my_list[len(my_list)-pos-1])
print(new_list)
