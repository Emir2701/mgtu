'''защита 9-й работы: Дана целочисленная матрица размера NxM. Требуется сформировать новую матрицу размера KxL, 
переписав в неё все элементы исходной по порядку. Если в новую матрицу все элементы не поместятся - лишние отбросить, 
если ячеек в новой матрице больше - дополнить нулевыми элементами.'''

n_str_1 = int(input('Введите количество строк матрицы 1: '))
n_col_1 = int(input('Введите количество столбцов матрицы 1: '))

matrix_1 = [[0]*n_col_1 for i in range(n_str_1)]

# Ввод массива
for i in range(n_str_1):
	for j in range(n_col_1):
		matrix_1[i][j] = int(input('Введите {}-ый символ {}-й строки матрицы D: '.format(j + 1, i + 1)))

# Вывод массива
print('Введенная матрица 1:')
for i in range(n_str_1):
	for j in range(n_col_1):
		print('{:<10}'.format(matrix_1[i][j]), end=' ')
	print()

n_str_2 = int(input('Введите количество строк матрицы 2: '))
n_col_2 = int(input('Введите количество столбцов матрицы 2: '))

matrix_2 = [[0]*n_col_2 for i in range(n_str_2)]


if n_str_2 > n_str_1 or n_col_2 > n_col_1:
	for i in range(n_str_1):
		for j in range(n_col_1):
			matrix_2[i][j] = matrix_1[i][j]
else:
	for i in range(n_str_2):
		for j in range(n_col_2):
			matrix_2[i][j] = matrix_1[i][j]

print('Матрица 2:')
for i in range(n_str_2):
	for j in range(n_col_2):
		print('{:<10}'.format(matrix_2[i][j]), end=' ')
	print()