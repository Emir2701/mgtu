a = list(map(int, input('Введите массив a: ').split()))
b = list(map(int, input('Введите массив b: ').split()))
c = list(map(int, input('Введите массив c: ').split()))


for i in b:
	if i in c:
		b.remove(i)

for i in c:
	if i in a:
		a.remove(i)
		

for i in b:
	if i in a:
		a.remove(i)

if len(a) >= 2:
	a[0], a[-1] = a[-1], a[0]
print('Элементы, которые есть в a, но их нет в b и c. \
Первый и полследний элементы меняются местами при необходимости:', a)