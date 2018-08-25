'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
	'''
	clean the given string
	'''
    words = string.lower().strip().replace('\'', '')
    regex = re.compile('[^a-z, 0-9]')
    words = regex.sub("", words)
    return words
def main():
	'''
	clean up the given string removing the special characters
	'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
