
# 4. Swap minimum and maximum items in list

numbers = [12, 3, 20, 50, 8, 40, 27, 100]
print('Current List: ', numbers)

# Easiest Way
print('\nMinimum Element in List: ', min(numbers))
print('Maximum Element in List: ', max(numbers))

minIndex = numbers.index(min(numbers))
maxIndex = numbers.index(max(numbers))

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

temp = numbers[minIndex]
numbers[minIndex] = numbers[maxIndex]
numbers[maxIndex] = temp

print('\nUpdated List: ', numbers)

