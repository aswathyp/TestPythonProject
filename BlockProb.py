# if else block -

rows = int(input('Enter # of Rows: '))
cols = int(input('Enter # of Cols: '))
pieces = int(input('Enter # of Pieces: '))

if (rows*cols < pieces):
    print('Not Possible')
if pieces%rows == 0 or pieces%cols == 0:
    print('Possible')
else:
    print('Not Possible')