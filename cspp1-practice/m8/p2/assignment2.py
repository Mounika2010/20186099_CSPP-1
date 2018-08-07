'''
@author : Mounika2010
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number
and returns the sum of digits of given number.

# This function takes in one number and returns one number.
'''

def sumofdigits(n_inp):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n_inp == 0:
        return 0
    return n_inp%10 + sumofdigits(n_inp//10)
    # Your code here

def main():
    '''
    sum of digits
    '''
    n_inp = input()
    print(sumofdigits(int(n_inp)))

if __name__ == "__main__":
    main()
