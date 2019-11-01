
# 5. Pairs are equal, count them as one

numList = [12, 3, 20, 20, 8, 40, 27, 27, 100]
print('Current List: ', numList)

uniqueCount = 0

count = len(numList)
if count % 2 != 0:
    count -= 1

for i in range(0, count, 2):
    if numList[i] == numList[i+1]:
        uniqueCount = uniqueCount + 1

print('Unique Count: ', uniqueCount)