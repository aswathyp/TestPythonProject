
# Even elements in the sequence

numbers = [12, 3, 20, 50, 8, 40, 27, 0]
evenElementCount = 0

print('\nCurrent List:', numbers, sep=' ')
print('\nEven elements in the sequence: ')

for num in numbers:
    if num % 2 == 0:
        print(num, end=' ')
        evenElementCount = evenElementCount + 1

print('\n\nTotal Count of Even Numbers: ', evenElementCount)
