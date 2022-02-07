# a = [1,2,3,4]
# num = int(input("enter needed index to input: "))
# for i in range(num, len(a) - 1):
# 	a[i] = a[i + 1]
# a.pop(-1)
# print(a)
# import functools
# arr = list(range(5))
# arr.pop(0)
# mult = functools.reduce(lambda x, y: x*y, arr)
# print(mult)
a = ["a", "b"]
b = [1, 2]
s = [(a[i], b[i]) for i in range(len(a))]	
s = dict(s)

print(s["a"], s["b"])
