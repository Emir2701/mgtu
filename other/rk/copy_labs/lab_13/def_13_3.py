from struct import *

print("Программа удаляет максимальное число в бинарном файле: ")
l = list(input("Введите целые числа через пробел: ").split())
l = list(map(int, l))

len_number = 4

string_format = '{:}i'.format(len(l))
len_str = calcsize(string_format) 
string = pack(string_format, *l)

file = open('def_13.bin', 'wb')
file.write(string)
file.close()

file = open('def_13.bin', 'rb')
temp = file.read(len_str)
file.close()

temp = unpack(string_format, temp)
print(temp)

index = temp.index(max(temp))

file = open('def_13.bin', 'rb+')
pointer = index * len_number
	
while pointer + len_number < len_str:
	file.seek(pointer + len_number)
	temp = file.read(len_number)
	file.seek(pointer)
	file.write(temp)
	pointer += len_number
file.truncate(len_str - len_number)
file.close()

len_str -= len_number
string_format = '{:}i'.format(len(l) - 1)


file = open('def_13.bin', 'rb')
temp = file.read(len_str)
file.close()

temp = unpack(string_format, temp)
print(temp)