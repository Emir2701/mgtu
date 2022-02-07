file_name = '1.txt'
file = open(file_name, 'r')
l = []
for s in file:
	l.append(sum(map(float, s.split())))

file.close()

file_name_2 = '2.txt'
file2 = open(file_name_2, 'w')
for i in l:
	file2.write(str(i) + '\n')
file2.close()
print('Числа из файла 1.txt построчно суммировались и записались в 2.txt')