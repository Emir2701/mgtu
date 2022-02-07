def func_3(l):
	print(l)
	k = int(input('Введите нужный номер элемента в массиве: '))
	k -= 1
	l.append(-1)
	for i in range(len(l) - 1, k, -1):
		l[i] = l[i - 1]

	n = float(input('Введите значание числа, которое нужно вставить в нужное место в массиве: '))
	
	l[k] = n
	print('Массив: {}'.format(l))
	return l 

l = [1.0, 2.0, 3.0, 4.0, 5.0]
func_3(l)