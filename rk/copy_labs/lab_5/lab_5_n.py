# y = -(2x)^2/2! + (2x)^4/4! -(2x)^6/6! ..

x = float(input('Введите значение аргумента: '))
eps = float(input('введите значение эпсилона: '))

itr = 1
elem = ((-1) * (2*x)**2) / 2
s = elem

if abs(elem) <= eps:
	print('Сумма равна 0.')

else:
	while abs(elem) > eps:
		itr += 1
		elem *= ((-1) * (2 * x)**2 ) / (2*itr * (2*itr - 1))
		s += elem
	print('Сумма равна:', s)
