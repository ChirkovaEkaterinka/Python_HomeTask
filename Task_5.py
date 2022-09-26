# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# xyz = [int(input('Введите X, Y, Z: '))
#           for i in range(3)]
# print(xyz)

# leftSide = not(xyz[0] or xyz[1] or xyz[2])
# rightSide = not xyz[0] and not xyz[1] and not xyz[2]
# result = leftSide==rightSide
# print(result)

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not(x or y or z)==(not x and not y and not z))
            print(x,y,z)