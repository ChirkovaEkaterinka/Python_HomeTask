# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from tkinter import N

def func_fibonacci(n):
    if n in (1,2):
        return 1
    else:
        return func_fibonacci(n-1) + func_fibonacci(n-2)

def get_list(n):
    list = []
    for i in range(-n, 0):
        if i*(-1) % 2 == 0:
            list.append(-(func_fibonacci(-i)))
        else:
            list.append(func_fibonacci(-i))
    list.append(0)
    for i in range (1,n+1):
        list.append(func_fibonacci(i))
    return list


n = int(input('задайте число: '))
print(get_list(n))
