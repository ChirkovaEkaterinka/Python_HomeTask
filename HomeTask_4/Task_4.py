# # Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# # Пример:
# # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random
# num = int(input('Какой старшей степени будет многочлен? '))
# def generate_polynom(num: int):
#     if num > 0:
#         num1=random.randint(0,100)
#         str_1 = f"{num1}*x^{num}"
#         for i in reversed(range(2,num)):
#             num1=random.randint(0,100)
#             if num1 != 0:
#                 str_1 += f" + {num1}*x^{i}"
#         num1=random.randint(0,100)
#         if num1 != 0:
#             str_1 += f" + {num1}*x"
#         num1=random.randint(0,100)
#         if num1 != 0:
#             str_1 += f" + {num1} = 0"
#         else:
#             str_1 += f"{str_1} = 0"
#         return str_1
# result = generate_polynom(num)
# print(result)

# my_file = open('File.txt', 'w')
# my_file.write(result)
# my_file.close()


from random import randint

power = int(input('Введите натуральную степень многочлена (наивысшая степень в полиноме): '))


def polinom(power):
    with open('file.txt', 'w') as polinom:
        for i in range(power, -1, -1):
            koef = randint(0, 100)
            if i > 0:
                if koef > 0:
                    polinom.write(f'{str(koef)}x^{str(i)} + ')
            else:
                if koef > 0:
                    polinom.write(f'{str(koef)} = 0')
                else:
                    polinom.write(' = 0')
polinom(power)