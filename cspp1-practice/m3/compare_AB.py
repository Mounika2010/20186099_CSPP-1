'''
@author : Mounika2010
This program compares two variables
'''
varA = 8
varB = 7
if (type(varA)== str or type(varB)== str):
    print("string involved")
elif varA>varB:
    print("bigger")
elif varA==varB:
    print("equal")
elif varA<varB:
    print("smaller")
