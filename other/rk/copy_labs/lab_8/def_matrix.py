# matrix = []
# m = int(input('str '))
# n = int(input('col '))
# for i in range(m):
# 	matrix.append([])
# 	for j in range(n):
# 		matrix[i].append(int(input('введите {} элемент {}-й строки '.format(j + 1, i + 1))))



# for i in range(m):
# 	for j in range(n):
# 		print(matrix[i][j],end=' ')
# 	print()
def prime(x):
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

while True:
	if prime(int(input())):
		print('prime')
	else:
		print('not prime')