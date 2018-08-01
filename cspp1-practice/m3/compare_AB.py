'''
@author : Mounika2010
This program compares two variables
'''
VAR_A = 8
VAR_B = 7
if (isinstance(VAR_A, str) or isinstance(VAR_B, str)):
    print("string involved")
elif VAR_A > VAR_B:
    print("bigger")
elif VAR_A == VAR_B:
    print("equal")
else:
    print("smaller")
