def same_first_digit(x, y):
    '''
    return True, if first digit in both the numbers are equal
    otherwise return False
    '''
    temp1 = str(abs(x))
    temp2 = str(abs(y))
    i=0
    if temp1[i] == temp2[i]:
            return True
    return False 

def main():
    x = int(input())
    y = int(input())
    print(same_first_digit(x,y))

main()