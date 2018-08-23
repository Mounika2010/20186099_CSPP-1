'''
program that return True whether the given string has
more number of vowels than consonants, otherwise return False.
'''
def count_vowels(string_input):
	'''
	returns number of vowels in the given string parameter.
	'''
	count_vowels = 0
	vowels = "aeiou"
	for letter in string_input:
		if letter in vowels:
			count_vowels += 1
	return count_vowels


def count_consonants(string_input):
	'''
	returns number of consonants in the given string parameter.
	'''
	count_consonants = 0
	consonants = "bcdfghjklmnpqrstvwxyz"
	for letter in string_input:
		if letter in consonants:
			count_consonants += 1
	return count_consonants

def is_vowels_count_higher(string_input):
	'''
	returns true if vowels count is greater than consonants count, otherwise false
	'''
	temp1 = count_vowels
	temp2 = count_consonants
	if temp1 > temp2:
		return True
	else:
		return False


def main():
	string_input = input()
	print(is_vowels_count_higher(string_input))
