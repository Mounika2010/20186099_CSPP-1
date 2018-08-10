'''
multiples of 3
'''
def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3

for i in range(1,10):
    print(mult3(i))