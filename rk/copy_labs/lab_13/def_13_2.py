# Вводишь через пробел целые числа (4 байта). 
# Записываешь их в бинарный файл. В этом файле находишь максимальное число и удаляешь его
# Записать все сразу в файл в самом начале вроде можно
# Нельзя читать сразу все из файла
# По 4 бита только

import struct

print("Введите числа через пробел: ")

mas = list(map(int, input().split()))
f1 = open("def_13_2.bin", "wb")
f1.close()
f1 = open("def_13_2.bin", "rb+")
size = 0

for i in range(len(mas)):
	s = struct.pack("<i", mas[i])
	f1.write(s)
	size += 4

f1.seek(0)

max_num = int(struct.unpack("<i", f1.read(4))[0])
ind = 0
count = 4

while count < size - 4:    
	num = int(struct.unpack("<i", f1.read(4))[0])
	if num > max_num:
		max_num = num
		ind = count
	count += 4


for i in range(ind, size, 4):
	f1.seek(i + 4)
	s = f1.read(4)
	f1.seek(i)
	f1.write(s)

f1.seek(0)

for i in range(len(mas) - 1):
	print(struct.unpack("<i", f1.read(4))[0])



# import os

# f1 = open("/Users/natalakarakotova/Desktop/Python/f1.txt", "r")

# f2 = open("/Users/natalakarakotova/Desktop/Python/f2.txt", "w")

# count = len(f1.readline()) - 1



# for i in range(count):
# 	mas = []
# 	c=0
# 	for j in range(count):
# 		f1.seek(i + (count + 1)*c)
# 		ch = f1.read(1)
# 		mas.append(ch)
# 		print(ch)
# 		c += 1
# 	f2.write(''.join(mas[::-1]) + '\n')


		




