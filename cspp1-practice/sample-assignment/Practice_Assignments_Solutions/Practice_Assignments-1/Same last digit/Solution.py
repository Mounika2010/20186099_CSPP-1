def same_last_digit(x, y):
	'''
	return True, if last digit in both the numbers are equal
	otherwise return False
	'''
	return str(abs(x))[len(str(abs(x)))-1] == str(abs(y))[len(str(abs(y)))-1]

def main():
	x = int(input())
	y = int(input())
	print(same_last_digit(x,y))

main()