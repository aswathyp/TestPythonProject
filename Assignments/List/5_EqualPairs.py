
# 5. Pairs are equal, count them as one

numList = [int(i) for i in input('Enter Num List: ').split()]
print('Current List: ', numList)

uniquePairCount = 0

for i in range(0, len(numList)):
    if numList.count(numList[i]) % 2 == 0:
    uniquePairCount = numList.count(numList[i]) / 2
    if

print('Unique Pair Count: ', uniquePairCount)