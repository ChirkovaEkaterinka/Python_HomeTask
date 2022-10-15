# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите вещественное число: '))
res = [int(ele) for ele in str(num) if ele.isdigit()]
print("List of floating numbers is : " + str(res))
print(sum(res))
