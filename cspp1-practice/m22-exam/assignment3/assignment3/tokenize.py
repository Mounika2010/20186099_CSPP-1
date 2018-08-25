'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    tokenize
    '''
    dictionary = {}
    for word in string:
        if word not in dictionary:
            dictionary[word] = [string.count(word)]
    return dictionary    
def main():
    '''
    tokenize the string
    '''
    string = input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
