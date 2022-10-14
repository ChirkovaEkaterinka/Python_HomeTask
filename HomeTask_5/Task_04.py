# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import count
from unicodedata import digit

with open('encode_file.txt', 'w') as encode_file:
    encode_file.write('AAAAAGGGGGdUUUppGGGGGDDDDDcccWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')

with open('encode_file.txt', 'r') as encode_file:
    string = encode_file.readline()

def encode(s):
    encoding = ""  # сохраняет выходную строку
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
         # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
    return encoding

def decode(s):
    decoding = ''  # сохраняет выходную строку
    count = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count += s[i]
        else:
            decoding += s[i]*int(count)
            count = ''
    return decoding

with open('encode_file.txt', 'r') as encode_file:
    decoded_string = encode_file.read()

with open('decode_file.txt', 'w') as decode_file:
    encoded_string = encode(decoded_string)
    decode_file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + encode(decoded_string))





# with open('input.txt', 'r', encoding='utf-8') as input_file:
#     my_str = input_file.readline()
#     print(my_str)

# encode_string = encode(my_str)
# print(encode_string)

# with open('output.txt', 'w', encoding='utf-8') as output_file:
#     output_file.write(encode_string)

# with open('output.txt', 'r', encoding='utf-8') as output_file:
#     encoded_string = output_file.read()
#     print(encoded_string )


# decode_string = decode(encode_string)
# print(decode_string)

# with open('output.txt', 'w', encoding='utf-8') as output_file:
#     output_file.write(decode_string)
