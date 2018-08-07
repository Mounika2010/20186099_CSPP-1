'''
@author : Mounika2010
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.
'''

def gcd_recur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0 or b == 0:
        return 0
    if a%b == 0:
        return b
    elif b%a == 0:
        return a
    elif a > b:
        return gcd_recur(b, a%b)
    else:
        return gcd_recur(a, b%a)

    # Your code here
    


def main():
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
