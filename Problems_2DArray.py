
# 1. Problem - Generate a Square (n rows x n cols), Diagonal should have 1, upper should be 0 and below should be 2
rows = int(input('Enter square rows: '))
square = [[0] * rows for i in range(rows)]

print('Original Square:', end='\n')
for i in square:
    print(i, end='\n')

for i in range(rows):
    for j in range(rows):
        if i == j:
            square[i][j] = 1
        elif j < i:
            square[i][j] = 2
            square[j][i] = 0

print('Modified Square:', end='\n')
for i in square:
    print(i, end='\n')


# 2. Create a checkerboard pattern with '.' & '*' for n x m 2D array

rows = int(input('Enter n rows: '))
cols = int(input('Enter m cols: '))

TwoDArray = [[0] * rows for i in range(cols)]

for i in range(rows):    
    for j in range(cols):
        if i % 2 == 0:
            if j % 2 == 0:
                TwoDArray[i][j] = '.'
            else:
                TwoDArray[i][j] = '*'
        else:
            if j % 2 == 0:
                TwoDArray[i][j] = '*'
            else:
                TwoDArray[i][j] = '.'

print('CheckerBoard Array:', end='\n')
for i in TwoDArray:
    print(i, end='\n')
