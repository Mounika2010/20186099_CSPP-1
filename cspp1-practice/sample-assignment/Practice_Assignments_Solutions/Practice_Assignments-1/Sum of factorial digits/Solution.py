def fact(n):
	'''
	Use this function fact(n), which takes n as integer and returns n!
	'''
	if n == 0 or n == 1:
		return 1
	else:
		return n * fact(n-1)

def sum_of_fact(n):
	'''
	argument : n, integer type.
	return type: integer, which is the sum of factorial of each digit in n.
	example : 123 = 1! + 2! + 3! = 1 + 2 + 6 = 9
	Your task is to write code here and use fact(n) to find factorial for each digit.
	'''
	s = 0
	if n == 0:
		s = 1
	while n > 0:
		s += fact(n%10)
		n //= 10
	return s

def main():
	print(sum_of_fact(int(input())))

main()