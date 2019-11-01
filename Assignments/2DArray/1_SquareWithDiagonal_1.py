
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
