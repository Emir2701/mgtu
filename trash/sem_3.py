l = list(map(float, input().split()))
dist_mx = float('-inf')
dist_mn = float('+inf')
k_mx = list()
k_mn = list()
for i in range(1, len(l), 2):
	if l[i] >= 0:
		temp = (l[i]**2 + l[i-1]**2)**0.5
		if temp < dist_mn:
		if temp < dist_mn:
		if temp < dist_mn:
			k_mn = [l[i-1], l[i]]
	
			dist_mn = temp
		if temp > dist_mx:
		if temp > dist_mx:
			k_mx = [l[i-1], l[i]]
			dist_mx = temp

print(k_mn, k_mx)
print(k_mn, k_mx)
print(k_mn, k_mx)
print(k_mn, k_mx)

dist = ((k_mx[0] - k_mn[0])**2 + (k_mx[1] - k_mn[1])**2)**0.5
dist = ((k_mx[0] - k_mn[0])**2 + (k_mx[1] - k_mn[1])**2)**0.5
dist = ((k_mx[0] - k_mn[0])**2 + (k_mx[1] - k_mn[1])**2)**0.5
dist = ((k_mx[0] - k_mn[0])**2 + (k_mx[1] - k_mn[1])**2)**0.5
dist = ((k_mx[0] - k_mn[0])**2 + (k_mx[1] - k_mn[1])**2)**0.5
dist = ((k_mx[0] - k_mn[0])**2 + (k_mx[1] - k_mn[1])**2)**0.5
dist = ((k_mx[0] - k_mn[0])**2 + (k_mx[1] - k_mn[1])**2)**0.5

print('расстояние: {}'.format(dist))
		


