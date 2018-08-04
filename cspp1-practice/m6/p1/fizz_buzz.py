'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    @author : Mounika2010
    Read number from the input, store it in variable num.
    '''
    n = int(input())
    i = 1
    for i in n:
        if( (i%3) == 0 and (i%5) == 0):
            print("FizzBuzz")
        if((i%3) == 0):
            print("Fizz")
        if((i%5) == 0):
            print("Buzz")
        i += 1
    print(i)




if __name__ == "__main__":
    main()
