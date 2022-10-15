# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


#          0  1  2  3  4    5     6   7   8  9
my_list = [1, 4, 7, 9, 32, 687, 225, 789, 2, 0]

print('Исходный список: ', my_list)
#Вариант с List Comprehension
# print('Сумма элементов на нечет позициях = ', sum([my_list[x] for x in range(len(my_list)) if x % 2 != 0])) 

#Вариант с enumerate
res=[]
for count, i in enumerate(my_list):
    if count%2 != 0:
        res.append(i)
print('Сумма элементов на нечет позициях = ', sum(res))