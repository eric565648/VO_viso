import numpy as np
import math
import sys

def eulerAnglesToRotationMatrix(theta):
	R_x = np.array([[1,0,0],
					[0,math.cos(theta[0]),math.sin(theta[0])],
					[0,math.sin(theta[0]),math.cos(theta[0])]
					])
	R_y = np.array([[math.cos(theta[1]),0,math.sin(theta[1])],
					[0,1,0],
					[-math.sin(theta[1]),0,math.cos(theta[1])]
					])
	R_z = np.array([[math.cos(theta[2]),-math.sin(theta[2]),0],
					[math.sin(theta[2]),math.cos(theta[2]),0],
					[0,0,1]
					])
	R = np.dot(R_z, np.dot( R_y, R_x ))
	return R

def mainpart(inputfilename, ouputfilename):
	readfile = open(inputfilename, "r")
	outputfile = open(ouputfilename+".txt", "w")

	cont = readfile.readlines()
	output = ""

	for lines in cont:
		datas = lines.split(",")
		if datas[0][0] == '%':
			continue
		
		#translation part of a frame 
		translation = np.array([[float(datas[3]), float(datas[4]), float(datas[5])]])
		
		#transfer euler angle to 
		theta = np.array([float(datas[0]), float(datas[1]), float(datas[2])])
		RM = eulerAnglesToRotationMatrix(theta)
		matrix = np.concatenate((RM, translation.T), axis=1)

		for i in matrix:
			for j in i:
				output += str(j) + " "
		output += "\n"

	outputfile.write(output)

	outputfile.close()
	readfile.close()

if __name__== "__main__":
	print sys.argv[1], sys.argv[2]
	mainpart(sys.argv[1], sys.argv[2])
	#mainpart()
