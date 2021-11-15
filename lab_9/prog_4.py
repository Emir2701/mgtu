from cheak_func import *

def main():
	print('Условие:')
	print('-'*78)
	print('4. \nПоворот квадратной матрицы на 90 градусов по часовой стрелке, \nзатем на 90 \
градусов против часовой стрелки. \nВывести промежуточную и итоговую матрицу.')
	print('-'*78)
	n = correct_input('Введите размерность квадратной матрицы: ', 'int+')

	matrix = [[0]*n for i in range(n)]

	for i in range(n):
		for j in range(n):
			matrix[i][j] = correct_input('Введите {}-ый элемент {}-й строки: '.format(j + 1, i + 1), 'float')
	
	print('Введенная матрица:')
	for i in range(n):
		for j in range(n):
			print('{:<10.4}'.format(matrix[i][j]),end=' ')
		print()

	print('Поворот на 90 градусов по часовой стрелке:')
	for i in range(n//2):
		for j in range(i, n - i - 1):

			temp = matrix[n - j - 1][i]
			matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
			matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
			matrix[j][n - i - 1] = matrix[i][j]
			matrix[i][j] = temp

	for i in range(n):
		for j in range(n):
			print('{:<10.4}'.format(matrix[i][j]),end=' ')
		print()

	print('Поворот на 90 градусов против часовой стрелке:')
	for i in range(n//2):
		for j in range(i, n - i - 1):
			
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][n - i - 1] 
			matrix[j][n - i - 1] =  matrix[n - i - 1][n - j - 1]
			matrix[n - i - 1][n - j - 1] = matrix[n - j - 1][i]
			matrix[n - j - 1][i] = temp
			
	for i in range(n):
		for j in range(n):
			print('{:<10.4}'.format(matrix[i][j]),end=' ')
		print()

	

if __name__ == '__main__':
	main()	