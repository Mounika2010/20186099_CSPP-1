'''
@authour : Mounika2010
This prog prints numbers except the input and its multiples.
'''
N = int(input())
COUNT_NUM = 0
i = 2
while i <= 100:
    if i%N != 0:
        print(i)
    i += 1
