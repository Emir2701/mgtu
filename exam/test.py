# Удаление строки в файле
path = '1.txt'

f = open(path, 'r+')

num = int(input('Введите номер строки, которую хотите удалить: '))

s = f.readline()
count = 1
len_line = []

while count != num and s.strip() != '':
	len_line.append(len(s))
	s = f.readline()
	count += 1
s1 = s
print(s)
while s.strip() != '':
	s = f.readline()
	#print(s)
	f.seek(sum(len_line))
	f.write(s)
	len_line.append(len(s))
	f.seek(sum(len_line) + len(s1))

f.truncate(sum(len_line[:-1]))

f.close()




