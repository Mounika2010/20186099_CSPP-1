'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
	
	text = input()
	lines = ""
	for i in range(text):
    	lines += input() + "\n"

print lines	

if __name__ == '__main__':
    main()
