from cheak_func import *
	
def main():
	print('Условие:')
	print('-'*78)
	print('3. \nТранспонирование квадратной матрицы.')
	print('-'*78)
	n = correct_input('Введите размерность квадратной матрицы: ', 'int+')

	matrix = [[0]*n for i in range(n)]

	for i in range(n):
		for j in range(n):
			matrix[i][j] = correct_input('Введите {}-ый элемент {}-й строки: '.format(j + 1, i + 1), 'float')
	print('-'*78)
	for i in range(n):
		for j in range(n):
			print('{:<10.4}'.format(matrix[i][j]),end=' ')
		print()
	print('-'*78)

	for i in range(n):
		for j in range(i+1, n):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	for i in range(n):
		for j in range(n):
			print('{:<10.4}'.format(matrix[i][j]),end=' ')
		print()


if __name__ == '__main__':
	main()