'''
program that return True whether the given string has
more number of vowels than consonants, otherwise return False.
'''
def count_vowels(string_input):
	'''
	returns number of vowels in the given string parameter.
	'''
	return len([alphabet for alphabet in string_input if alphabet in 'aeiou'])


def count_consonants(string_input):
	'''
	returns number of consonants in the given string parameter.
	'''
	return len([alphabet for alphabet in string_input if alphabet not in 'aeiou'])


def is_vowels_count_higher(string_input):
	'''
	returns true if vowels count is greater than consonants count, otherwise false
	'''
	return count_vowels(string_input) > count_consonants(string_input)


def main():
	string_input = input()
	print(is_vowels_count_higher(string_input))
main()