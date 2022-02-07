mas = list(map(int, input().split()))

mas_1 = []

for i in range(len(mas)):
	if mas[i] not in mas_1:
		mas_1.append(mas[i])

count_ch = []

for i in range(len(mas_1)):
	count_ch.append(mas.count(mas_1[i]))
print(count_ch)
for i in range(len(count_ch)):
	if count_ch.count(count_ch[i]) > 1:
		print('Количество каждого элемента не уникально.')
		break
else:
	print('Количество каждого элемента уникально.')
