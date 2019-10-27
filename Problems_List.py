
# 1. Determine how many elements in sequence are > their both peers
numbers = [12, 3, 25, 56, 9, 18, 27, 0]
count = numbers.count()
greaterElementCount = 0

print('Elements greater than their neighbours: ')

for i in range(1, count - 1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        print(numbers[i])
        greaterElementCount = greaterElementCount + 1
    
print('Total Count: ' + greaterElementCount)

# 2. Swap adjacent items in pairs
numbers = [12, 3, 20, 50, 8, 40, 27, 0, 100]
print('List: ' + numbers)

for i in range(0, numbers.count(), 2):
    temp = numbers[i]
    numbers[i] = numbers[i+1]
    numbers[i+1] = temp
    
print('Updated List: ' + numbers)

# 3. Swap minimum and maximum items in list
numbers = [12, 3, 20, 50, 8, 40, 27, 0, 100]
print('Current List: ' + numbers)

minIndex, maxIndex = 0
minValue, maxValue = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < minValue:
        minIndex = i
        minValue = numbers[i]

    if numbers[i] > maxValue:
        maxIndex = i
        maxValue = numbers[i]

temp = numbers[minIndex]
numbers[minIndex] = numbers[maxIndex]
numbers[maxIndex] = temp
    
print('Updated List: ' + numbers)


# 4. Adjacent pairs are equal, count them as one
numList = [12, 3, 20, 50, 8, 40, 27, 0, 100]
print('Current List: ' + numList)
uniqueCount = 0

for i in range(0, len(numList), 2):
    if numList[i] == numList[i+1]:
        uniqueCount = uniqueCount + 1

print('Unique Count: ', uniqueCount)


# 5. Print the elements in list which appear only once, in the exact order
numList = [12, 3, 20, 50, 8, 40, 27, 0, 100]
print('Current List: ' + numList)
uniqueNumList = []

for i in range(0, len(numList)):
    uniqueFlag = False

    for j in range(1, len(numList)):
        if numList[i] == numList[j]:
            uniqueFlag = True
            break;

    if uniqueFlag:
        uniqueNumList.append(numList[i])

print('Unique Num List: ', uniqueNumList)
