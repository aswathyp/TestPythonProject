
# Determine how many elements in sequence are > their peers above
numbers = [12, 3, 25, 56, 9, 18, 27, 0]
count = numbers.count()
greaterElementCount = 0

print('Elements greater than their neighbours above: ')

for i in range(1, count):
    if numbers[i] > numbers[i-1]:
        print(numbers[i])
        greaterElementCount = greaterElementCount + 1
    
print('Total Count: ' + greaterElementCount)

# Even elements in the sequence ending with 0
numbers = [12, 3, 20, 50, 8, 40, 27, 0, 100]
evenWith0ElementCount = 0

print('Even elements ending with zero: ')

for num in numbers:
    if num % 2 == 0:
        print(num)
        evenWith0ElementCount = evenWith0ElementCount + 1
    
print('Total Count: ' + evenWith0ElementCount)

# Ladder of n steps

n = int(input('Enter number of ladder steps <= 9: '))

if n <= 9:
    continue
else:
    break

k = int(input('Enter kth step < n: '))

print('Ladder Steps: ')
for i in range(0, n):
    k = i
    for j in range(0, k):
        print(sep=' ')
    print('_', end='\n')


print('Ladder Steps with Integers: ')
for i in range(0, n):
    if i == k:
        for j in range(1, k + 1):
            print(j, sep='')
    print(i, sep=' ', end='\n')
