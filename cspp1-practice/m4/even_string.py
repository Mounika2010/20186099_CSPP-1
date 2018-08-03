'''
@author : Mounika2010
This program prints reverse of even characters of a string
'''
S = input()
LENGTH = len(S)
COUNT_STR = 0
i = 0
TEMP1 = ""
TEMP2 = ""
for i in S:
    if i%2 == 0:
        TEMP1 = TEMP1 + S[i]
    i += 1
    if i%2 != 0:
        TEMP2 = TEMP2 + S[i]
    i += 1
print(TEMP1)
print(TEMP2)
