'''
Write a python program to calculate the first 26 Fibonacci numbers and assign 
each Fibonacci number a letter in English by using Dictionaries.
(Keys as English alphabets and Values as Fibonacci numbers). Given a string as
input and calculate the sum of all the values of the characters that are associated with the
Fibonacci numbers from the given string. Write a function for finding the Fibonacci
numbers.
'''
import string

def building_dictionary():
	'''
	returns a dictionary with Keys as English alphabets and Values as Fibonacci numbers.
	example dictionary = {'a':0, 'b':1, 'c':1 .....}
	'''
	list_fibonacci_numbers = [fibonacci_numbers(i) for i in range(27)]
	lower_case_aplhabets_list = list(string.ascii_lowercase)
	return dict(zip(lower_case_aplhabets_list, list_fibonacci_numbers))

def fibonacci_numbers(n):
	'''
	function for finding the Fibonacci numbers,
	returns the fibonacci number
	example: The first six fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, ... 
	'''
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)

def sum_of_dictionary_values(string_input):
	'''
	calculates the sum of the values corresponding to the keys in dictionary, by 
	Iterating each alphabet in the string input. returns sum of all the values.

	'''
	dictionary = building_dictionary()
	return sum([dictionary[character] for character in string_input.lower() if character in dictionary ])



def main():
	string_input = input()
	print(sum_of_dictionary_values(string_input))

main()