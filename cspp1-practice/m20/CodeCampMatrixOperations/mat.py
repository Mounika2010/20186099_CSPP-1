'''
matrix addition and mul
'''
m = int(input("Enter rows"))
n = int(input("Enter columns"))
matrix = []
for i in range(0,n):
	matrix.append([])
for i in range(0,m):
	for j in range(0,n):
		matrix[i].append(j)
		matrix[i][j] = 0
for i in range(0,m):
	for j in range(0,n):
		print('entry on row: ',i+1, 'column:', j+1)
		matrix[i][j] = int(input())
print(matrix)