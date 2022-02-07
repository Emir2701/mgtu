# Вводишь через пробел целые числа (4 байта). 
# Записываешь их в бинарный файл. 
# В этом файле находишь максимальное число и удаляешь его


from struct import *

file = open('def_13.bin', 'wb')
file.close


file = open('def_13.bin', 'ab')

n = int(input("Введите количество чисел: "))

size_file = 0
size_int = 4

for i in range(n):

	number = int(input("Введите {} число: ".format(i + 1)))
	
	number = pack("i", number)
	file.write(number)
	size_file += size_int

file.close




file = open('def_13.bin', 'rb')

first_number = file.read(size_int)
first_number = unpack("i", first_number)
max_number = first_number
ind_max = 0
pointer = 0

for i in range(size_int, size_file, size_int):

	number = file.read(size_int)
	number = unpack("i", number)
	if number >= max_number:
		max_number = number
		pointer = file.tell()
		


file.close()



print(pointer)
file = open('def_13.bin', 'rb+')

	
for i in range(pointer, size_file, size_int):
	file.seek(i)
	temp = file.read(size_int)
	file.seek(i - size_int)
	file.write(temp)

size_file -= size_int

file.truncate(size_file)

file.close()


file = open('def_13.bin', 'rb')

for i in range(0, size_file, size_int):
	number = file.read(size_int)
	number = unpack("i", number)
	print(number)


file.close()




