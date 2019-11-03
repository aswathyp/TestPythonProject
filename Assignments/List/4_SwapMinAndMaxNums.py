
# 4. Swap minimum and maximum items in list

numbers = [int(i) for i in input('Enter Num List: ').split()]
print('Current List: ', numbers)

print('\nMinimum Element in List: ', min(numbers))
print('Maximum Element in List: ', max(numbers))

minIndex = numbers.index(min(numbers))
maxIndex = numbers.index(max(numbers))

numbers[minIndex], numbers[maxIndex] = numbers[maxIndex], numbers[minIndex]

print('\nUpdated List: ', numbers)

# Longer way
# minIndex, maxIndex = 0, 0
# minValue, maxValue = numbers[0], numbers[0]
#
# for i in range(1, len(numbers)):
#     if numbers[i] < minValue:
#         minIndex = i
#         minValue = numbers[i]
#
#     if numbers[i] > maxValue:
#         maxIndex = i
#         maxValue = numbers[i]
#