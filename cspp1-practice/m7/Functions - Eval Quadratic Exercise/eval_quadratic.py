'''
@author : Mounika2010
# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value
of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.
'''
def eval_quadratic(a_int, b_int, c_int, x_int):
    '''
    This code returns a value of quadratic equation"
    '''
    return a_int * (x_int**2) + b_int * x_int +c_int

def main():
    '''
    "This code returns a value of quadratic eq"
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for x_int in range(len(data)):
        temp = str(data[x_int]).split('.')
        if temp[1] == '0':
            data[x_int] = int(float(str(data[x_int])))
        else:
            data[x_int] = data[x_int]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
