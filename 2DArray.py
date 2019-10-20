# Two-Dimensional List
a = [[1,2], [3,4], [5,6]]

# Via Indices
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print('\n')

# Via Elements
for row in a:
    for element in row:
        print(element, end=' ')
    print('\n')

# Generate 2D
n = 3
m = 4
arr = [[0] * m] * n #doesn't create a memory for the n rows
arr[0][2] = 5
print('2D: ', arr, sep='\n')
a = [[0] * m for i in range(n)] # Generator contruct and creates memory of 2D list

for i in range(n):
    b.append([0] * m)   # Creates a memory and assign the sub-list

# Input 2D Array
rows = int(input('Enter number of rows: '))
arrList = []

for i in range(rows):
    print('Reading ', i , 'th row: ')
    arrList.append([int(j) for j in input().split()])
    print(i, 'th row is: ', arrList[i])

print('Array List:', arrList, sep=' ')

arrList = [[int(j) for j in input.split() if j!=-1] for i in range(n)]