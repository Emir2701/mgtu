'''
def func(x):
	return x**2

def integral(x):
	return x**3/3


start = float(input("Введите начальное значение: "))
end = float(input("Введите конечное значение: "))

eps = float(input("Введите точность: "))


def trap(start, end, n):

	dx = (end - start)/n 
	summ = 0
	x_start = start
	while x_start < end:
		summ += ((func(x_start) + func(x_start + dx))/2) * dx
		x_start += dx
	
	return summ

count = 1
value = integral(end) - integral(start)

while not abs(trap(start, end, count) - value) < eps:
    count <<= 1

print('Интеграл будет вычеслен с точностью {:.4}, если количество участков разбиения будет равно: {}'.format(eps, count))
print('Значение при данном разбиении: {:.4}'.format(trap(start, end, count)))

'''

s = ' dfsfs dfsdf2*2fgdfgf 5/ 2 df'

l = s.split() 