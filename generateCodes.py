import random
import string


# Generate amount random strings of length
# Return a
def generateCodes(amount, length = 8):
	results = []
	str_base = 'qwertyuiopasdfghjkzxcvbnmQWERTYUOPASDFGHJKLZXCVBNM'
	for i in range(amount):
		results.append(''.join(random.sample(str_base + string.digits, length)))
		#results.append(''.join(random.sample(string.ascii_letters + string.digits, length)))
	return results


if __name__ == '__main__':
	check()

def check():
	t = 3000
	suc = 0
	for i in range(t):
		ls = generateCodes(50000, 8)
		if len(ls) != len(set(ls)):
			suc += 1
	print(suc)
	print(suc/t)