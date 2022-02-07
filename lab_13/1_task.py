def main():
	with open("in1.txt", "r") as f1, open("in2.txt", "r") as f2, open("outT1.txt", "w") as fout:
		_int_1 = f1.readline().strip()
		_int_2 = f2.readline().strip()
		#print(_int_1, _int_2)
		while True:
			
			if _int_1 != "" and _int_2 != "":

				if int(_int_1) <= int(_int_2):
					fout.write(_int_1 + "\n")
					_int_1 = f1.readline().strip()
				else:
					fout.write(_int_2 + "\n")
					_int_2 = f2.readline().strip()

			elif _int_1 != "" and _int_2 == "":
				fout.write(_int_1 + "\n")
				_int_1 = f1.readline().strip()
			elif _int_1 == "" and _int_2 != "":
				fout.write(_int_2 + "\n")
				_int_2 = f2.readline().strip()
			else:
				break

					


main()