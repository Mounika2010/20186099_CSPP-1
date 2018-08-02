'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2
@author : Mounika2010
'''
def main():
    '''
    @author : Mounika2010
    This program prints bob
    '''
    s_str = input()
    i = 0
    count_k = 0
    value_bob = "bob"
    for i in range(len(s_str)-2):
        if s_str[i] + s_str[i+1] + s_str[i+2] == value_bob:
            count_k += 1
    print(count_k)
    # the input string is in s
    # remove pass and start your code here
if __name__ == "__main__":
    main()
