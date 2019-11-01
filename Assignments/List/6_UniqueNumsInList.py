
# 6. Print the elements in list which appear only once, in the exact order

numList = [12, 3, 20, 50, 8, 3, 27, 12, 20]
print('Current List: ', numList)

duplicateNumList = []

for i in range(len(numList)):
    for j in range(i+1, len(numList)):
        if numList[i] == numList[j]:
            duplicateNumList.append(numList[i])

print('Duplicate Num List: ', duplicateNumList)

uniqueNumList = []

# # Print distinct numbers from list
# distinctNumList = []
# for i in range(0, len(numList)):
#     try:
#         if distinctNumList.index(numList[i]):
#             pass
#     except ValueError:
#         distinctNumList.append(numList[i])
#
# print('Distinct Num List: ', distinctNumList)