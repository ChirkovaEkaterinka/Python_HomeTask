# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# data = []
# with open("To_task_5_1.txt") as f:
#     for line in f:
#         data.append(line)
#         print(data)
# # newdata = ''.join([i for i in data if i.isdigit()])
# data1 = [s.replace('*x', '') for s in data]
# data2 = [s.replace('= 0', '') for s in data1]
# print(data2)

# data3 = [elem for line in data2 for elem in line.split()]
# print(data3)
# data4=[]
# for i in range(1, len(data3), 2):
#     if data4[i] =='-' or data4[i] =='+':
#         data4.append(data4[i-1]+data4[i])
# print(data4)    


with open("To_task_5_1.txt", 'r') as polynom1:
    my_str1 = polynom1.read()
with open("To_task_5_2.txt", 'r') as polynom2:
    my_str2 = polynom2.read()

my_list1 = my_str1.split('+')
my_list2 = my_str2.split('+')

dictionary1 = {}

for i in range(len(my_list1)):
    if 'x' in my_list1[i]:
        posX = my_list1[i].find('x')
        dictionary1[int(my_list1[i][posX + 2:])] = int(my_list1[i][:posX])
    else:
        posEqualy = my_list1[i].find(' =')
        dictionary1[0] = int(my_list1[i][:posEqualy])

print(dictionary1)
dictionary2 = {}

for i in range(len(my_list2)):
    if 'x' in my_list2[i]:
        posX = my_list2[i].find('x')
        dictionary2[int(my_list2[i][posX + 2:])] = int(my_list2[i][:posX])
    else:
        posEqualy = my_list2[i].find(' = ')
        dictionary2[0] = int(my_list2[i][:posEqualy])

print(dictionary2)

maxDegree = max(max(dictionary1.keys()), max(dictionary2.keys()))

with open('To_task_5_3_res.txt', 'w') as two_polinom:
    for i in range(maxDegree, 0, -1):
        koef = 0
        if i in dictionary1.keys():
            koef += dictionary1[i]
        if i in dictionary2.keys():
            koef += dictionary2[i]
        if koef != 0:
            two_polinom.write(f'{koef}x^{i} + ')
    koef = 0
    if 0 in dictionary1.keys():
        koef += dictionary1[0]
    if 0 in dictionary2.keys():
         koef += dictionary2[0]
    if koef != 0:
         two_polinom.write(f'{koef} = 0')