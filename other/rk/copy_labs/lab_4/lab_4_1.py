# y = x**6 - 2 * x**5 + 1.7 * x**4 - 4.7 * x**3 - 0.8 * x**2 + 4.26 * x - 2

# x_0 = -1.1
# h = 0.1
# x_n = 1.2

scale = -1
width = 80
x_0 = float(input('Введите x_0: '))
h = float(input('Введите x_n: '))
x_n = float(input('Введите h: '))
eps = 1e-8
list_x = []
list_y = []


while not 4 <= scale <= 8:
	scale = int(input('Введите количество засечек: '))
	if 4 <= scale <= 8:
		break
	else:
		print('Ошибка')


print(20*'-')
print('|{: ^7} | {: ^7} |'.format('x', 'y'))
print(20*'-')



i = x_0

while i <= x_n:
	
	y = i**6 - 2 * i**5 + 1.7 * i**4 - 4.7 * i**3 - 0.8 * i**2 + 4.26 * i - 2

	list_y.append(round(y, 4))
	list_x.append(round(i, 4))

	if abs(i) < eps:
		print('|  {: <6.4}| {: <7.4} |'.format(0.0, y))
	else:
		print('|  {: <6.4}| {: <7.4} |'.format(i, y))
	i += h

print(20*'-')


s = 6*' '




