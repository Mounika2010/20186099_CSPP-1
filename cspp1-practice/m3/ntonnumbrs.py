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


iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 