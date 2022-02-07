array = list(map(int, input().split()))

for i in range(1, len(array)):
	temp = array[i]
	j = i - 1
	while j >= 0 and temp < array[j]:
		array[j + 1] = array[j]
		j -= 1
	array[j + 1] = temp

print(array)


