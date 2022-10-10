# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Какого целого числа будем искать простые множители? '))
res_list = []
i=2
num_to_print = num
while i<=num:
    if num%i==0:
        res_list.append(i)
        num//=i
        i=2
    else:
        i+=1
print(f'Простые множители числа {num_to_print} в списке: {res_list}')    
