'''
@author : Mounika2010
# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.
'''
def is_in(char, astr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if char == astr[0]:
        return True
    elif len(astr) == 1:
        return False
    else:
        return is_in(char, astr[1: ])
    # Your code here
   

def main():
    data = input()
    data = data.split(",")
    print(is_in((data[0][0]), data[1]))


if __name__ == "__main__":
    main()
