n = int(input('Введите размерность квадратной матрицы: '))

matrix = [[0]*n for i in range(n)]

for i in range(n):
	for j in range(n):
		matrix[i][j] = float(input('Введите {}-ый элемент {}-й строки: '.format(j + 1, i + 1)))


print("Введенная матрица: ")

for i in range(n):
	for j in range(n):
		print('{:<10.4}'.format(matrix[i][j]),end=' ')
	print()

mx = matrix[0][n-1]
mx_ind_col = n - 1

for i in range(1, n):
	j = (n - 1)- i
	if mx < matrix[i][j]:
		mx = matrix[i][j]
		mx_ind_col = j

number_col = mx_ind_col + 1

for i in range(n):
	matrix[i][mx_ind_col] += number_col

print("Матрица со увеличенными значениями элеменотов столбца, \n\
в котором находится макисмиальный элемент побочной диагонали, на номер столбца: ")

for i in range(n):
	for j in range(n):
		print('{:<10.4}'.format(matrix[i][j]),end=' ')
	print()
