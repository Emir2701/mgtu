# y = x^2
x0 = float(input('ведите начальную точку: '))
x1 = float(input('ведите конечную точку: '))
x = float(input('ведите шаг точку: '))


print('{}>'.format('-'*50))


j = 0
for i in range(50):
    if (i + 1) % x == 0 and x0 < i < x1:
        j += 1
        print('|{}*'.format(' '*int(round(j * x)**2)))
    else:
        
        print('|')

print('\/')
