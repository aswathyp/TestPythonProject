
# 3. Swap adjacent items in pairs

numbers = [int(i) for i in input('Enter Num List: ').split()]
print('List: ', numbers)

for i in range(1, len(numbers), 2):
    numbers[i-1], numbers[i] = numbers[i], numbers[i-1]

print('\nUpdated List: ', numbers)

# numbers = [12, 3, 20, 50, 8, 40, 27, 0, 100]
# print('List: ', numbers)
#
# count = len(numbers)
# if count % 2 != 0:
#     count -= 1
#
# for i in range(0, count, 2):
#     temp = numbers[i]
#     numbers[i] = numbers[i + 1]
#     numbers[i + 1] = temp
#
# print('\nUpdated List: ', numbers)

