
# Determine how many elements in sequence are > their peers above

numbers = [12, 3, 25, 56, 9, 18, 27, 0]
greaterElementCount = 0

print('\nCurrent Number List:', numbers, sep=' ')

print('\nElements greater than their neighbours above: ')

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i], end=' ')
        greaterElementCount = greaterElementCount + 1

print('\n\nTotal count greater than their peers above: ', greaterElementCount)

# While Loop - Sequence of numbers ending with 0.