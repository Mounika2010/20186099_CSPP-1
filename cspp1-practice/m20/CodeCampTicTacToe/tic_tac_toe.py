
















def input_validation(matrix):

    for i in matrix:
        for j in i:
            if j not in 'x.o':
                return False
    return True


def invalid_game(matrix):

    if matrix.count('x') > 5 or if matrix.count('o') > 5:
        return False
def valid_rules_are_followed(matrix):

    x_count = 0
    x_count = 0
    for row in matrix:
        x_count += row.count('x')
        o_count += row.count('o')

    if o_count > 5 or x_count > 5:
        



def read_mx():
    
    grid = []
    rows = 3
    for _ in range(rows):
        grid.append(input().split(" "))
    return grid

def main():
    '''
    Main function
    '''
    print(input_validation(read_mx()))
main()









