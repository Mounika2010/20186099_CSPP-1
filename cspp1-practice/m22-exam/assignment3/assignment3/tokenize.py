'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    tokenize
    '''
    dictionary = {}
    for letter in string:
        if letter not in dictionary:
            dictionary[letter] = [string.count(letter)]
            
def main():
    '''
    tokenize the string
    '''
    string = input()
    print(tokenize(string()))

if __name__ == '__main__':
    main()
