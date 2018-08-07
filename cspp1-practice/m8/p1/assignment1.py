'''
@author : Mounika2010
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def fact_rec(n_var):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n_var == 1:
        return 1
    if n_var == 0:
        return 0
    return n_var * fact_rec(n_var-1)
    # Your code here

def main():
    '''
    factorial
    '''
    n_var = input()
    print(fact_rec(int(n_var)))  

if __name__ == "__main__":
    main()
