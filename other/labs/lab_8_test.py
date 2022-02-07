n = 2
m = 3

a = [[0] * m for i in range(n)]

print(a)

# Шимшир Эмирджан ИУ7-13Б 1 задача
'''
n = int(input('Введите размерность матрицы: '))

matrix = [[0]*n for i in range(n)]

for i in range(n):
	for j in range(n):
		matrix[i][j] = float(input("Введите {}-ый элемент {}-й строки: ".format(j + 1, i + 1)))

print('Введенная матрица:')
for i in range(n):
	for j in range(n):
		print('{:<10.4}'.format(matrix[i][j]),end=' ')
	print()
'''
'''
n = int(input('Размерность '))

m = [[0]*n for i in range(n)]

for i in range(n):
	for j in range(n):
		m[i][j] = float(input('Введите элемент '))

for i in range(n):
	for j in range(n):
		print('{:<10.4}'.format(m[i][j]),end=' ')
	print()
print()

mx = m[0][n-1]

mx_ind = n-1
for i in range(1, n):
	j = n - 1 - i
	
	if m[i][j] > mx:
		mx = m[i][j]
		mx_ind = j

for i in range(n):
	m[i][mx_ind] += mx_ind + 1

for i in range(n):
	for j in range(n):
		print('{:<10.4}'.format(m[i][j]),end=' ')
	print()
'''