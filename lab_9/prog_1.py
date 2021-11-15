import math
from cheak_func import *


def main():
	
	print('Условие:')
	print('-'*78)
	print('1. \nДаны массивы D и F. Сформировать матрицу A по формуле a_jk = sin(d_j+f_k).\n\
Определить среднее арифметическое положительных чисел каждой строки матрицы\nи количество \
элементов, меньших среднего арифметического. \nРезультаты записать соответственно в массивы AV и L. \n\
Напечатать матрицу A в виде матрицы и рядом столбцы AV и L.')
	print('-'*78)
	n_D = correct_input('Введите количество элементов массива D: ', 'int+')
	l_D = [0] * n_D

	for i in range(n_D):
		input_text = 'Введите {}-й элемент списка: '.format(i+1)
		l_D[i] = correct_input(input_text, 'float')

	print('Список D: {}'.format(l_D))

	n_F = correct_input('Введите количество элементов массива F: ', 'int+')
	l_F = [0] * n_F

	for i in range(n_F):
		input_text = 'Введите {}-й элемент списка: '.format(i+1)
		l_F[i] = correct_input(input_text, 'float')

	print('Список F: {}'.format(l_F))

	n_str = n_D
	n_col = n_F

	A = [[0]*n_col for i in range(n_str)]

	for j in range(n_str):
		for k in range(n_col):
			A[j][k] = round(math.sin(l_D[j] + l_F[k]), 4)
	
	AV = []
	L = []
	for i in range(n_str):
		s = 0
		n = 0
		for j in range(n_col):
			if A[i][j] > 0:
				s += A[i][j]
				n += 1
		if n == 0:
			AV.append('нет среднего')
			L.append('нет среднего')
		else:
			avr = s/n
			n = 0
			for j in range(n_col):
				if A[i][j] < avr:
					n += 1
			AV.append(round(avr, 4))
			L.append(n)

	s = ''
	print(AV)
	print(L)
	for i in range(n_str):
		for j in range(n_col):
			s += '{:<14.4}'.format(A[i][j])
		s += '|{:<14}|{:<14}\n'.format(AV[i], L[i])
	print(s, end = '')
		
      
if __name__ == '__main__':
	main()

