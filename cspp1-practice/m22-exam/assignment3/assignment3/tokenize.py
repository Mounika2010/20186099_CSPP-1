'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
	dictionary = {}
    for letter in string:
    	if letter not in dictionary:
    		dictionary[letter] = string.count(letter)
            
def main():
    string = input()

if __name__ == '__main__':
    main()
