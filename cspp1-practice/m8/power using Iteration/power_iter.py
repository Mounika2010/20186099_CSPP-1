'''
@author : Mounika2010
# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two
numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.
'''

def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    x = 1
    while exp > 0:
        x = (x * base)
        exp -= 1
    return x    

def main():
    '''
    takes in two numbers and returns one num.
    '''
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1]))) 

if __name__ == "__main__":
    main()
