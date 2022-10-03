# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from pickletools import int4

num_binary = int(input('Введите целое число: '))
# print(bin(num_binary))
binary_code = ''
while num_binary > 0:
    binary_code = str(num_binary % 2) + binary_code
    num_binary = num_binary // 2
print('Двоичное представление числа: ', binary_code)
