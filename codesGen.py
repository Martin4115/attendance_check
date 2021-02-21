import generateCodes
import printAndSave

def codesGen(amount, batch_id):
	labels = generateCodes.generateCodes(amount)
	printAndSave.codes2pdf(labels, batch_id)
	printAndSave.codes2txt(labels, batch_id)
	print("Generated " + str(amount) + " codes both on pdf and txt file")


if __name__ == '__main__':
	codesGen(30, 1)
