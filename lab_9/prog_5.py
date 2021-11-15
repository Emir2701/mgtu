from cheak_func import *

def main():
	print('Условие:')
	print('-'*78)
	print('5. \nПодсчитать в каждой строке матрицы D количество элементов, \n\
превышающих суммы элементов соответствующих строк матрицы Z. \n\
Разместить эти количества в массиве G, \n\
умножить матрицу D на максимальный элемент массива G. \n\
Напечатать матрицу D до и после преобразования, а также массив G.')
	print('-'*78)
	n = correct_input('Введите количество строк матриц D и Z: ', 'int+')
	d = correct_input('Введите количество столбцов матрицы D: ', 'int+')
	z = correct_input('Введите количество столбцов матрицы Z: ', 'int+')

	matrix_D = [[0]*d for i in range(n)]
	matrix_Z = [[0]*z for i in range(n)]

	for i in range(n):
		for j in range(d):
			matrix_D[i][j] = correct_input('Введите {}-ый элемент {}-й строки матрицы D: '.format(j + 1, i + 1), 'float')
	
	for i in range(n):
		for j in range(z):
			matrix_Z[i][j] = correct_input('Введите {}-ый элемент {}-й строки матрицы Z: '.format(j + 1, i + 1), 'float')

	print('Введенная матрица D:')
	for i in range(n):
		for j in range(d):
			print('{:<10}'.format(matrix_D[i][j]), end=' ')
		print()

	print('Введенная матрица Z:')
	for i in range(n):
		for j in range(z):
			print('{:<10}'.format(matrix_Z[i][j]), end=' ')
		print()

	list_G = [0]*n

	for i in range(n):
		s = sum(matrix_Z[i])
		for j in range(d):
			if matrix_D[i][j] > s:
				list_G[i] += 1

	print('Список G:')
	print(*list_G)

	mx = max(list_G)
	for i in range(n):
		for j in range(d):
			matrix_D[i][j] = mx * matrix_D[i][j]

	print('Матрица D:')
	for i in range(n):
		for j in range(d):
			print('{:<10}'.format(matrix_D[i][j]), end=' ')
		print()


if __name__ == '__main__':
	main()	