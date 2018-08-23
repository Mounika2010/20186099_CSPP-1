def sum_of_digits(x):
	'''
	integer parameter x.
	return the sum of all the digits of given number
	'''
	result = 0
	while x > 0:
		rem = x % 10
		result = result + rem
		x = x//10
	return result

def main():
	x = int(input())
	print(sum_of_digits(x))

main()