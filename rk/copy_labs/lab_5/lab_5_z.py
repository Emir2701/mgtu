

x = float(input('Введите x: '))
eps = float(input('Введите точность эпсилон: '))
count = int(input('Введите количество итераций: '))
h = int(input('Введите шаг: '))

element = 1
s = 0

if abs(element) <= eps:
	print('Сумма бесконечного ряда - 0, вычислена за 1 итерацию')
else:

	print(36*'-')
	print('| № итерации |{: ^10}|{: ^10}|'.format('t', 's'))
	print(36*'-')
	

	for i in range(0, count):

		element *= (-1)* (2*x)**2/(2*(i + 1)*(2*(i + 1) - 1))

		s += element

		if i % h == 0:
			print('| {: <10} |{: ^10.4}|{: ^10.4}|'.format(i + 1, element, s))

		if abs(element) <= eps:

			print(36*'-')
			print('Сумма бесконечного ряда - {}, вычислена за {} итераций(ю)'.format(s, i + 1))
			break

	else:
		print(36*'-')
		print('За указанное число итераций необходимой точности достичь не удалось')



