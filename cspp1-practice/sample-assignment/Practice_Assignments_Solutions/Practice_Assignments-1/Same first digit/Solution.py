def same_first_digit(x, y):
	'''
	return True, if first digit in both the numbers are equal
	otherwise return False
	'''
	return str(abs(x))[0] == str(abs(y))[0]

def main():
	x = int(input())
	y = int(input())
	print(same_first_digit(x,y))

main()