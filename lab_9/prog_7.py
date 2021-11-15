from cheak_func import *

def main():
	def matrix_input(input_text):
		text = input(input_text)
		while True:
			if len(text) != 1:
				print('В строчке несколько символов: ')
				text = input(input_text)
			else:
				return text

	print('Условие:')
	print('-'*78)
	print('7. \nДана матрица символов. \n\
Заменить в ней все гласные английские буквы на точки.')
	print('-'*78)

	n_str = correct_input('Введите количество строк матрицы: ', 'int+')
	n_col = correct_input('Введите количество столбцов матрицы: ', 'int+')

	matrix = [[0]*n_col for i in range(n_str)]
	
	for i in range(n_str):
		for j in range(n_col):
			matrix[i][j] = matrix_input('Введите {}-ый символ {}-й строки матрицы D: '.format(j + 1, i + 1))

	print('Введенная матрица:')
	for i in range(n_str):
		for j in range(n_col):
			print('{:<10}'.format(matrix[i][j]), end=' ')
		print()
	
	s = 'aeyuioAEYUIOяыуаеиоюэёЯЫУАИЕОЮЭЁ'

	for i in range(n_str):
		for j in range(n_col):
			if matrix[i][j] in s:
				matrix[i][j] = '.'

	print('Матрица после преобразований:')
	for i in range(n_str):
		for j in range(n_col):
			print('{:<10}'.format(matrix[i][j]), end=' ')
		print()


if __name__ == '__main__':
	main()