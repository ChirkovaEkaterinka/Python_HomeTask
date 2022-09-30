# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите вещественное число: ')
sum = 0
count = 0
while n.is_integer() == False:
    if count <= 3:
        n = n*10
        count += 1
    else:
        break
print(n)
while n % 10 != 0:
    sum = sum + n % 10
    n=n//10
print(sum)

# print(type(n))
# for i in n:
#     if i !='.':
#         sum+=int(i)
# print(sum)
