# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

my_list = [random.randrange(0, 10)
           for _ in range(int(input('Введите кол-во элементов списка: ')))]
print('Сгенерируемый список: ', my_list)
print(my_list)
res_list = []
for elem in my_list:
    if elem not in res_list:
        res_list.append(elem)
print(res_list)