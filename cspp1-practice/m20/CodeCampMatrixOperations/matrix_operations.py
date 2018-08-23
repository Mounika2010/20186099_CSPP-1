def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    rows = len(matrix_one)
    columns = len(matrix_two[0])
    mult_matrix = generate_resultant_matrix(rows, columns)

def generate_resultant_matrix(rows, columns):
	add_matrix = [[0] * columns] * rows
	return add_matrix

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    rows = len(matrix_one)
    columns = len(matrix_one[0])
    add_matrix = generate_resultant_matrix(rows, columns)
    res = []
    for i in range(len(rows)):
        row = []
        for j in range(len(columns[0])):
            row.append(rows[i][j] + columns[i][j])
        res.append(row)
    return add_matrix

    	


 
#in python initilization is needed before indexing.
    matrix1=[[0 for j in range(0,n)] for i in range(0,m)]   # matrix 1 initialization with 0s
    matrix2=[[0 for j in range(0,n)] for i in range(0,m)]    #matrix 2 intialization with 0s
    res_matrix=[[0 for j in range(0,n)] for i in range(0,m)] # matrix for storing result
    print("enter first matrix elements")
    for i in range(0,m):
        for j in range(0,n):
            matrix1[i][j]= int(input("enter an element"))
    print("enter second matrix elements ")    
    for i in range(0,m):
        for j in range(0,n):
            matrix2[i][j]=int(input("enter an element"))
        
    for i in range(0,m):
        for j in range(0,n):
            res_matrix[i][j]=matrix1[i][j]+matrix2[i][j]
 
#print input matrices
    print(" matrix 1")
    print_matrix(matrix1)
    print(" matrix 2")
    print_matrix(matrix2)
        
# printing resultant matrix
    print("resultant matrix after adding")
    print_matrix(res_matrix)

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
	matrix = []
	list_input = input().split(',')
	rows, columns = int(list_input[0]), int(list_input[1]):
	for _ in range(rows):
		list_matrix_row = input().split()
		if columns == len(list_matrix_row):
			matrix.append([int(i) for i in list_matrix_row])
		else:
			print("Error: Invalid input for the matrix")
			return None
	return matrix



def main():
    # read matrix 1
	m=int(input("enter rows"));
    n=int(input("enter columns"));
    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
