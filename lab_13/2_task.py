# отсортировать числа в in1.txt и записать в outT1.txt
def find_min_larger(min_int, fin):
	fin.seek(0)
	_int = fin.readline().strip()
	new_min = float("+inf")
	while _int != "":
		if min_int < int(_int) < new_min:
			new_min = int(_int)

		_int = fin.readline().strip()
	return new_min

def write_new_min(new_min, fout, fin):
	fin.seek(0)
	_int = fin.readline().strip()
	while _int != "":
		if new_min == int(_int):

			fout.write(str(_int) + "\n")
		_int = fin.readline().strip()


def main():
	with open("in1.txt", "r") as fin, open("out.txt", "w") as fout:
		min_int = float("-inf")
		while True:
			new_min = find_min_larger(min_int, fin)
			if new_min == float("+inf"):
				break
			write_new_min(new_min, fout, fin)
			min_int = new_min

main()
