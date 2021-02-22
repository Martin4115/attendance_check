import generateCodes
import printAndSave
import sys
import random

def codesGen(amount, batch_id):
	labels = generateCodes.generateCodes(amount)
	printAndSave.codes2pdf(labels, batch_id)
	printAndSave.codes2txt(labels, batch_id)
	print("Generated " + str(amount) + " codes both on pdf and txt file")


if __name__ == '__main__':
	argv = sys.argv
	if len(argv) == 1:
		codesGen(30, random.randint(10000000,99999999))
	elif len(argv) == 2:
		num = int(argv[1])
		codesGen(num, random.randint(10000000,99999999))
	elif len(argv) == 3:
		codesGen(int(argv[1]), argv[2])
	else:
		print("Invalid argument")
