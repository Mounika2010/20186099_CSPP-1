'''
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    flag = 0
    if int_input<0:
        int_input=abs(int_input)
        flag = 1
        digi_prod = 1
    for i in range(len(str(int_input))):
        del i
        B = int_input%10
        digi_prod = digi_prod * B
        int_input = int_input//10
    if flag == 1:
        print('-' + str(digi_prod))
    else:
        print(digi_prod)

if __name__ == "__main__":
    main()
