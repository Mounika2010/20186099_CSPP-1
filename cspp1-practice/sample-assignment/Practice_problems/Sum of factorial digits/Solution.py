def fact(n):
	'''
	Use this function fact(n), which takes n as integer and returns n!
	'''
		if rem > 1:
		return rem * fact(rem-1)
	else:
		return 1


def sum_of_fact(n):
	'''
	argument : n, integer type.
	return type: integer, which is the sum of factorial of each digit in n.
	example : 123 = 1! + 2! + 3! = 1 + 2 + 6 = 9
	Your task is to write code here and use fact(n) to find factorial for each digit.
	'''
	sum = 0
	while n > 0:
		rem = n % 10
		sum = sum + fact(rem)
		n = n // 10
	return sum

def main():
	print(sum_of_fact(int(input())))

main()