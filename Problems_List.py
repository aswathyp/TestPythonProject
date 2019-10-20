
# Determine how many elements in sequence are > their both peers
numbers = [12, 3, 25, 56, 9, 18, 27, 0]
count = numbers.count()
greaterElementCount = 0

print('Elements greater than their neighbours: ')

for i in range(1, count - 1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        print(numbers[i])
        greaterElementCount = greaterElementCount + 1
    
print('Total Count: ' + greaterElementCount)

# Swap adjacent items in pairs
numbers = [12, 3, 20, 50, 8, 40, 27, 0, 100]
print('List: ' + numbers)

for i in range(0, numbers.count(), 2):
    temp = numbers[i]
    numbers[i] = numbers[i+1]
    numbers[i+1] = temp
    
print('Updated List: ' + numbers)

# Swap minimum and maximum items in list
numbers = [12, 3, 20, 50, 8, 40, 27, 0, 100]
print('List: ' + numbers)

for i in range(0, numbers.count()):
    temp = numbers[i]
    numbers[i] = numbers[i+1]
    numbers[i+1] = temp
    
print('Updated List: ' + numbers)
