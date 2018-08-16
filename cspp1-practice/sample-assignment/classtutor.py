l = []
def sum_elements_in_the_list(l):
	return sum(l)

def length_of_list(l):
	return len(l)

def mean_of_values(l):
	list_sum = sum_elements_in_the_list(l):
	number_of_elements = length_of_list(l)
	return list_sum / number_of_elements


def medain_of_values():
	l.sort()
	n = length_of_list(l)
	if n % 2 != 0:
		return l[n//2]
	else:
		return (l[n//2] + l[n//2 + 1]) / 2

































