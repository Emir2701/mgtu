x = float(input())
n = int(input())

element = x
s = x
print(element, s)
for i in range(1, n):
	a = (2*i - 1)**2
	b = element**2
	c = (2*i*(2*i + 1))
	element *= (a * b )/ c
	s += element
	print('a = {}, b = {}, c = {}'.format(a, b, c))
	print(element, s)