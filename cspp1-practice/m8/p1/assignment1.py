'''
@author : Mounika2010
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
and returns the factorial of given number.

# This function takes in one number and returns one number.
'''

def fact_rec(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n == 1:
        return 1
    return n * fact_rec(n-1)
    # Your code here


def main():
    n = input()
    print(fact_rec(int(n)))    

if __name__ == "__main__":
    main()