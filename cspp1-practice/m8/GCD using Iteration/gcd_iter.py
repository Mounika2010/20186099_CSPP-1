'''
@author : Mounika2010
# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers
and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.
'''

def gcd_iter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0 or b == 0:
        return 0
    elif a == 1 or b == 1:
        return 1
    elif a%b == 0:
        return b
    elif b%a == 0:
        return a
    temp = 0
    for i in range(max(a, b)):
        i = 1
        a%b == 0 and b%a == 0
        temp = i
    return temp



    # Your code here
    



def main():
    '''
    gcd of two numbers
    '''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1]))) 

if __name__ == "__main__":
    main()