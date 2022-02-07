# Удаление строки в файле
path = '/Users/natalakarakotova/Desktop/Python/1.txt'

# f = open(path, 'r+')

# num = int(input('Введите номер строки, которую хотите удалить: '))

# s = f.readline()
# count = 1
# len_line = []

# while count != num and s.strip() != '':
# 	len_line.append(len(s))
# 	s = f.readline()
# 	count += 1
# s1 = s
# while s.strip() != '':
# 	s = f.readline()
# 	print(s)
# 	f.seek(sum(len_line))
# 	f.write(s)
# 	len_line.append(len(s))
# 	f.seek(sum(len_line) + len(s1))

# f.truncate(sum(len_line[:-1]))

# f.close()


# Добавление строки в файл
f = open(path, 'r+')
num = int(input('Введите номер строки, которую хотите добавить: '))
num -= 1

line = input('Введите строку, которую хотите добавить: ')

len_line = len(line) + 1

count_lines = []

s = f.readline()

while s.strip() != '':
	count_lines.append(len(s))
	s = f.readline()

count = len(count_lines) - 1

if len_line > len(str(count_lines[-1])):
	f.write('*' * (len_line - len(str(count_lines[-1]))))

while count != num - 1:
	f.seek(sum(count_lines[:count]))
	s = f.readline()
	f.seek(sum(count_lines[:count]) + len_line)
	f.write(s)
	count -= 1

f.seek(sum(count_lines[:num]))
f.write(line + '\n')


f.close()



