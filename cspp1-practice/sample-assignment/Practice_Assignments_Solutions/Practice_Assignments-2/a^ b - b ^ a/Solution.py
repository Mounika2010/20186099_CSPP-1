def is_power_differences_odd(a, b):
	'''
	return boolean value
	After finding diffrences of the a^b and b^a, If it is odd, return True
	else return False
	'''
	a_power_b = finding_a_power_of_b(a, b)
	b_power_a = finding_a_power_of_b(b, a)
	if (a_power_b - b_power_a) % 2 != 0:
		return True
	else:
		return False


def finding_a_power_of_b(a, b):
	'''
	return number, which is a^b (a power of b)
	'''
	return a**b



def main():
	'''
	Takes Input and call the function
	'''
	n = int(input())
	m = int(input())
	print(is_power_differences_odd(n, m))

main()
