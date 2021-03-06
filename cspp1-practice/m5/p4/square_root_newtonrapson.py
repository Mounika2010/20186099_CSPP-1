'''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
    '''
    @author : Mounika2010
    this program prints the cube root using newton raphson method
    '''
    x_i = int(input())
    epsilon = 0.01
    guess = x_i/2.0
    while abs(guess*guess - x_i) >= epsilon:
        guess = guess - (((guess**2) - x_i)/(2*guess))
    print(str(guess))

if __name__ == "__main__":
    main()
