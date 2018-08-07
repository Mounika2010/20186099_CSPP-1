'''
@author : Mounika2010
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
number and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def fact_rec(n_input):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n_input == 1:
        return 1
    return n_input * fact_rec(n_input-1)
    # Your code here

def main():
    '''
    Factorial using python
    '''
    n_input = input()
    print("Factorial Is:", fact_rec(int(n_input)))

if __name__ == "__main__":
    main()
