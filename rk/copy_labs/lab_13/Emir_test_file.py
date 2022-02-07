# в файле записана квадратная символьная матрица (строки с равным кол-вом символов без пробелов)
# в новый файл нужно вывести эту матрицу повернутую на 90 градусов вправо
file_1 = "Emir_test_file.txt"
file_2 = "Emir_test_file_1.txt"


f1 = open(file_1, "r")

f2 = open(file_2, "w")

count = len(f1.readline()) - 1



for i in range(count):
	mas = []
	c=0
	for j in range(count):
		f1.seek(i + (count + 1)*c)
		ch = f1.read(1)
		mas.append(ch)
		print(ch)
		c += 1
	f2.write(''.join(mas[::-1]) + '\n')


