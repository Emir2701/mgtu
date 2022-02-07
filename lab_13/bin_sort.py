import struct
import os

def input_file(path):
	arr = list(map(int, input("Введите числа: ").split()))
	
	data = struct.pack("{}i".format(len(arr)), *arr)
	with open(path, "wb") as f:
		f.write(data)

def print_file(path):
	size = os.path.getsize(path)
	with open(path, "rb") as f:
		arr = list(struct.unpack("{}i".format(size//4), f.read(size)))
	print(*arr)

def sort_file_insert(path):
	# for i in range(1, len(arr)):
	# 	temp = arr[i]
	# 	j = i - 1
	# 	while j >= 0 and arr[j] > temp:
	# 		arr[j + 1] = arr[j]
	# 		j -= 1
	# 	arr[j + 1] = temp
	with open(path, "rb+") as f:
		size = os.path.getsize(path)
		for i in range(4, size, 4):
			f.seek(i)
			temp = struct.unpack("i", f.read(4))[0]
			j = i - 4
			f.seek(j)
			j_el = struct.unpack("i", f.read(4))[0]
			while j >= 0 and j_el > temp:
				f.seek(j + 4)
				f.write(struct.pack("i", j_el))
				j -= 4
				if j >= 0:
					f.seek(j)
					j_el = struct.unpack("i", f.read(4))[0]

			f.seek(j + 4)
			f.write(struct.pack("i", temp))

def sort_file_choose(path):

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
			
			f.seek(min_ind)
			a_min_ind = struct.unpack("i", f.read(4))[0]
			f.seek(i)
			a_i = struct.unpack("i", f.read(4))[0]

			f.seek(i)
			f.write(struct.pack("i", a_min_ind))
			f.seek(min_ind)
			f.write(struct.pack("i", a_i))

def f_del(f, i, size):
	# print_file(path)
	
	for j in range(i, size - 4, 4):
		f.seek(j + 4)
		elem = struct.unpack("i", f.read(4))[0]
		# print(elem)
		f.seek(j)
		f.write(struct.pack("i", elem))
	f.truncate(size - 4)
	return size - 4 




def del_negat(path):
	size = os.path.getsize(path)
	with open(path, "rb+") as f:
		i = 0
		while i < size:
		
			f.seek(i)
			# print_file(path)
			_int = struct.unpack("i", f.read(4))[0]
			print("i", i)
			print(_int)
			if _int < 0:
				
				size = f_del(f, i, size)
				i -= 4
			i += 4

def del_negat_2(path):
	size = os.path.getsize(path)
	with open(path, "rb+") as f:
		i = 0
		while i < size:
		
			f.seek(i)
			_int = struct.unpack("i", f.read(4))[0]
			print(_int)
			if _int < 0:
				
				for j in range(i, size - 4, 4):
					f.seek(j + 4)
					elem = struct.unpack("i", f.read(4))[0]
					#print(elem)
					f.seek(j)
					f.write(struct.pack("i", elem))
				f.truncate(size - 4)
				size -= 4
				i -= 4
			i += 4
def add_sum_to_i(f, size, i, _sum):
	for j in range(size, i, -4):
		f.seek(j - 4)
		temp = f.read(4)
		f.seek(j)
		f.write(temp)
	f.seek(i + 4)
	f.write(struct.pack("i", _sum))

def add_sum_after_negat(path):
	size = os.path.getsize(path)
	with open(path, "rb+") as f:
		_sum = 0
		i = 0
		while i < size:
			f.seek(i)
			_int = struct.unpack("i", f.read(4))[0]
			if _int >= 0:
				_sum += _int
				print(_int)
			else:
				add_sum_to_i(f, size, i, _sum)
				i += 4
				size += 4
			i += 4


#print_file("out.txt")
def main():
	path = "out.txt"
	input_file(path)
	
	#print_file(path)
	#sort_file_insert(path)
	#sort_file_choose(path)
	#del_negat(path)
	#del_negat_2(path)
	add_sum_after_negat(path)
	print_file(path)
main()

