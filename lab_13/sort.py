l = [4, 8, 2, 9, 5, 1]

n = len(l)
# for i in range(n - 1):
# 	for j in range(n - 1 - i):
# 		if l[j] > l[j + 1]:
# 			l[j], l[j + 1] = l[j + 1], l[j]
print(l)

for i in range(n):
	min_id = i
	for j in range(i + 1, n):
		if l[j] < l[min_id]:
			min_id = j
	l[i], l[min_id] = l[min_id], l[i]
print(l)