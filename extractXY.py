
readfile = open("output/mono_06.txt", "r")
outputfilex = open("06_x", "w")
outputfilez = open("06_z", "w")

cont = readfile.read()
x = ""
z = ""

print cont

i = 0
j = 0
k = 0
h = 0
while j != 104930:
	
	if i == 4:
		if cont[j] != ',':
			x+=cont[j]
		k+=1
		#print cont[j]

	elif i==6:
		if cont[j] != ',':
			z+=cont[j]
		h+=1
		#print cont[j]

	if cont[j] == '\n':
		x+=cont[j]
		k+=1
		z+=cont[j]
		h+=1
		i = 0
	if cont[j] == ',':
		i+=1

	j+=1

outputfilex.write(x)
outputfilez.write(z)

outputfilex.close()
outputfilez.close()
readfile.close()

