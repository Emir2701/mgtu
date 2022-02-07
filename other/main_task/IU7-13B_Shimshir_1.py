# В файле in.txt записаны дробные числа в 8-ричной системе счисления, 
# по одному в строке, разделитель целой и дробной части - точка.
# Требуется:
# 1. Перевести числа из исходного файла в 16-ричную систему счисления и 
#переписать их в файл out1.txt по одному в строке в том же порядке.
# 2. Переписать строки файла out1.txt в файл out2.txt, отсортировав их по увеличению длин.

# Обработку файлов производить построчно, содержимое файла читать в память целиком запрещается. 
#Списки, множества, словари, кортежи для сортировки не использовать.


def from_8_to_16(string):
	array = string.split(".")
	#print(array)
	l1 = []
	l2 = []
	for i in array[0]:
		a = bin(int(i))
		a = a[2:]
		for i in range(3 - len(a)):
			a = "0" + a
		l1.append(a)
	for i in array[1]:
		a = bin(int(i))
		a = a[2:]
		for i in range(3 - len(a)):
			a = "0" + a
		l2.append(a)
	#print(l1)
	#print(l2)
	s1 = ''
	for i in l1:
		s1 += i
	s2 = ''
	for i in l2:
		s2 += i

	#print(s1)
	#print(s2)
	i_1_10 = int(s1, 2)
	i_2_10 = int(s2, 2)
	#print(i_1_10, i_2_10)
	i_1_16 = hex(i_1_10)[2:]
	i_2_16 = hex(i_2_10)[2:]
	string = i_1_16 + '.'  + i_2_16
	return string


f1 = open("in.txt", 'r')
f2 = open("out1.txt", 'w')
line = f1.readline()
while line.strip() != "":
	f2.write(from_8_to_16(line.strip()) + '\n')
	line = f1.readline()
f1.close()
f2.close()
