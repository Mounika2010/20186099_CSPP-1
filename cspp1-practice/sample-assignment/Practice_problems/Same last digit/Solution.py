def same_last_digit(x, y):
	'''
	return True, if last digit in both the numbers are equal
	otherwise return False
	'''
	temp1 = str(x)
	temp2 = str(y)
	length1 = len(temp1)
	length2 = len(temp2)
	temp3 = temp1[-1]
	temp4 = temp2[-1]
	if temp3 == temp4:
		return True
	else:
		return False

def main():
	x = int(input())
	y = int(input())
	print(same_last_digit(x,y))

main()