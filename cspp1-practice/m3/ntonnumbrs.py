'''
@author: Mounika2010
This program prints n to -n numbers
'''
n = int(input())
i = 0
for i in range(-i, i+1):
    print(i)

n = int(input())
i = -n


count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)