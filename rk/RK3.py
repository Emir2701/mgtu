# РК 3 Задание 1

# В двух файлах находятся неубывающие последовательности целых чисел
# Записать в третий файл из двух данных неуб. посл. из всех чисел
# Работать с файлами построчно, в памяти не более 1 строки из каждого

# path1 = '/Users/natalakarakotova/Desktop/Python/1.txt'
# path2 = '/Users/natalakarakotova/Desktop/Python/2.txt'
# path3 = '/Users/natalakarakotova/Desktop/Python/3.txt'


# f1 = open(path1, 'r', encoding='utf-8')
# f2 = open(path2, 'r', encoding='utf-8')
# f3 = open(path3, 'w', encoding='utf-8')

# s1 = f1.readline()
# s2 = f2.readline()

# while s1.strip() != '' or s2.strip() != '':
# 	if s1.strip() != '' and s2.strip() != '':
# 		if int(s1) < int(s2):
# 			f3.write(s1)
# 			s1 = f1.readline()
# 		else:
# 			f3.write(s2)
# 			s2 = f2.readline()
# 	elif s1.strip() != '':
# 		f3.write(s1)
# 		s1 = f1.readline()
# 	else:
# 		f3.write(s2)
# 		s2 = f2.readline()


# f1.close()
# f2.close()
# f3.close()


# ___________________________________________________
# РК 3 Задание 2
# Отсортировать числа в бинарном файле методом вставок

import os
import struct

path = '1.bin'

mas = list(map(int, input().split()))
f1 = open(path, 'wb')

for i in range(len(mas)):
	f1.write(struct.pack('<i', mas[i]))
f1.close()

f1 = open(path, 'rb+')

size = os.path.getsize(path)

for i in range(4, size, 4):
	f1.seek(i)
	ch = struct.unpack('<i', f1.read(4))[0]
	j = i - 4
	f1.seek(j)
	ch2 = struct.unpack('<i', f1.read(4))[0]
	while j >= 0 and ch2 > ch:
		f1.write(struct.pack('<i', ch2))
		j -= 4
		f1.seek(j)
		ch2 = struct.unpack('<i', f1.read(4))[0]
	f1.seek(j + 4)
	f1.write(struct.pack('<i', ch))

f1.seek(0)

for i in range(0, size, 4):
	print(struct.unpack('<i', f1.read(4))[0])
	
f1.close()

