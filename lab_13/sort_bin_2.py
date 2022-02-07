# Отсортировать числа в бинарном файле
import struct
import os


def input_file(path):
	arr = list(map(int, input("Введите числа: ").split()))

	data = struct.pack("{}i".format(len(arr)), *arr)
	with open(path, "wb") as f:
		f.write(data)

def output_file(path):
	size = os.path.getsize(path)
	with open(path, "rb") as f:
		print(*list(struct.unpack("{}i".format(size//4), f.read(size))))

def select_sort(path):
	# for i in range(len(a)):
	# 	min_ind = i
	# 	for j in range(i, len(a)):
	# 		if a[j] < a[min_ind]:
	# 			min_ind = j
	# 	a[i], a[min_ind] = a[min_ind], a[i]
	size = os.path.getsize(path)
	with open(path, "rb+") as f:
		for i in range(0, size, 4):
			min_ind = i
			for j in range(i, size, 4):
				f.seek(min_ind)
				a_min_ind = struct.unpack("i", f.read(4))[0]
				f.seek(j)
				a_j = struct.unpack("i", f.read(4))[0]
				if a_j < a_min_ind:
					min_ind = j
			f.seek(i)
			a_i = f.read(4)
			f.seek(min_ind)
			a_min_ind = f.read(4)
			f.seek(i)
			f.write(a_min_ind)
			f.seek(min_ind)
			f.write(a_i)





def main():
	path = "in1.txt"
	input_file(path)
	select_sort(path)
	output_file(path)
main()