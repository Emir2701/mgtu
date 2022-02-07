from struct import *

# создание файла
file = open("Emir_bin.bin", "wb")
file.close

# заполнение файла
file = open("Emir_bin.bin", "ab")

n = int(input("Введите количество чисел: "))
size_file = 0
size_int = 4

for i in range(n):
	number = int(input("Введите {} число: ".format(i + 1)))

	number = pack("i", number)
	file.write(number)
	size_file += size_int

file.close()

# поиск максимального числа
file = open("Emir_bin.bin", "rb")

first_number = file.read(size_int)
first_number = unpack("i", first_number)

max_number = first_number
pointer = file.tell()

for i in range(size_int, size_file, size_int):
	number = file.read(size_int)
	number = unpack("i", number)
	if number >= max_number:
		max_number = number
		pointer = file.tell() 


file.close()

# удаление максимального числа
file = open("Emir_bin.bin", "rb+")

for i in range(pointer, size_file, size_int):

	file.seek(i)
	number = file.read(size_int)
	file.seek(i - size_int)
	file.write(number)

size_file -= size_int 
file.truncate(size_file)



file.close()

# вывод файла
file = open("Emir_bin.bin", "rb")

for i in range(0, size_file, size_int):
	number = file.read(size_int)
	number = unpack("i", number)
	print(number[0])

file.close()

