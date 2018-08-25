def sum_of_digits(x):
	'''
	integer parameter x.
	return the sum of all the digits of given number
	'''
	s = 0
	while x > 0:
		s += (x%10)
		x //= 10
	return s


def main():
	x = int(input())
	print(sum_of_digits(x))

main()