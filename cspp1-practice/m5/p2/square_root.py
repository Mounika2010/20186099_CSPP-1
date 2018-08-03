'''
@author : Mounika2010
# Write a python program to find the square root of the given number
# using approximation method
'''
def main():
    '''
    @author : Mounika2010
    This program prints square root of a number using apprx method"
    '''
    square = float(input())
    epsilon = 0.01
    guess = 0.0
    increment = 0.0001
    num_guesses = 0
    while abs(guess**2-square) >= epsilon:
        guess += increment
        num_guesses += 1
    print("num_guesses=", num_guesses)
    if abs(guess**2-square) >= epsilon:
        print("Failed on square root of", square)
    else:
        print(guess, "is close to the square root of", square)
    #your code here

if __name__ == "__main__":
    main()
