# Шимшир Эмирждан ИУ7-13Б

# Программа предназначена для формирования матрицы C путём построчного перемножения матриц A и B одинаковой 
# размерности и вывода суммы всех элементов в столбцах матрицы C

# Данные, принимаемые на вход программой:
# n_str  – количество строк в матрицах  
# n_col – количество столбцов в матрицах 


# Переменные для вычислений:
# matrix_A – матрица A
# matrix_B – матрица B
# matrix_C – матрица C
# array_V – массив V, содержащий сумму элментов в каждом столбце матрицы C

from cheak_func import *

def main():
	#------------------------------------------------------------------------------------------------
	print('Условие:')
	print('-'*78)
	print('8. \nСформировать матрицу C путём построчного перемножения матриц A и B \n\
одинаковой размерности (элементы в i-й строке матрицы A умножаются на соответствующие элементы в \n\
i-й строке матрицы B), потом сложить все элементы в столбцах матрицы C и записать их в массив V.')
	print('-'*78)
	#------------------------------------------------------------------------------------------------

	n_str = correct_input('Введите количество строк матриц: ', 'int+')
	n_col = correct_input('Введите количество столбцов матриц: ', 'int+')

	matrix_A = [[0]*n_col for i in range(n_str)]
	matrix_B = [[0]*n_col for i in range(n_str)]
	matrix_C = [[0]*n_col for i in range(n_str)]
	
	# Ввод массивов
	for i in range(n_str):
		for j in range(n_col):
			matrix_A[i][j] = correct_input('Введите {}-ый элемент {}-й строки матрицы A: '.format(j + 1, i + 1), 'float')

	for i in range(n_str):
		for j in range(n_col):
			matrix_B[i][j] = correct_input('Введите {}-ый элемент {}-й строки матрицы B: '.format(j + 1, i + 1), 'float')

	for i in range(n_str):
		for j in range(n_col):
			matrix_C[i][j] = matrix_A[i][j] * matrix_B[i][j]

	# Вывод массивов
	print('Введенная матрица A:')
	for i in range(n_str):
		for j in range(n_col):
			print('{:<10}'.format(matrix_A[i][j]), end=' ')
		print()

	print('Введенная матрица B:')
	for i in range(n_str):
		for j in range(n_col):
			print('{:<10}'.format(matrix_B[i][j]), end=' ')
		print()

	print('Матрица С:')
	for i in range(n_str):
		for j in range(n_col):
			print('{:<10}'.format(matrix_C[i][j]), end=' ')
		print()

	array_V = [0] * n_col 
	
	for j in range(n_col):
		for i in range(n_str):
			array_V[j] += matrix_C[i][j]

	print('Массив V:')
	print(*array_V)

if __name__ == '__main__':
	main()



