

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
