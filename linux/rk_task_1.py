
file_1 = "base.bin"
file_2 = "base_out.bin"


f1 = open(file_1, "r")
f2 = open(file_2, "w")

for s in f1:
	#print(s)
	s = s.split(".")
	
	


	for i in range(len(s) - 1):
		f2.write(s[i].strip() + ".\n")

	f2.write(s[-1].strip() + " ")

f1.close()
f2.close()
