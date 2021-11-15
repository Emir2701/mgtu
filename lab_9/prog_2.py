from cheak_func import *
	
def main():

	print('Условие:')
	print('-'*78)
	print('2. \nНайти максимальное значение над главной диагональю \n\
и минимальное - под побочной диагональю.')
	print('-'*78)
	n = correct_input('Введите размерность квадратной матрицы: ', 'int+')

	matrix = [[0]*n for i in range(n)]

	for i in range(n):
		for j in range(n):
			matrix[i][j] = correct_input('Введите {}-ый элемент {}-й строки: '.format(j + 1, i + 1), 'float')

	for i in range(n):
		for j in range(n):
			print('{:<10.4}'.format(matrix[i][j]),end=' ')
		print()

	l_up_main = []
	l_down_not_main = []
	for i in range(n):
		for j in range(i + 1, n):
			l_up_main.append(matrix[i][j])

	for i in range(n):
		for j in range(n-1, n-1 - i, -1):
			l_down_not_main.append(matrix[i][j])
	print('Максимум над главной диагональю: {}'.format(max(l_up_main)))
	print('Минимум под побочной диагональю: {}'.format(min(l_down_not_main)))



if __name__ == '__main__':
	main()