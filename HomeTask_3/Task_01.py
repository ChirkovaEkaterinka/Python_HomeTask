# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random


def my_sum_odd_pos(n):
    my_sum = 0
    for pos in range(1, len(n), 2):
        my_sum += n[pos]
    return my_sum


my_list = [random.randint(-100, 100)
           for _ in range(int(input('Введите кол-во элементов списка: ')))]
print('Сгенерируемый список: ', my_list)
print(my_sum_odd_pos(my_list))
# my_sum = 0
# for pos in range(0, len(my_list), 2):
#     my_sum = my_sum + my_list[pos]
# print(my_sum)
