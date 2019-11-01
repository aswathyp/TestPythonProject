
s = 'abcdefg'

#print(s[1])
#print(s[::-1])
#print(s[1:6:2])

# A string contains h letter at least twice. Remove first and last occurence as well as remove of chars between them

testWord = input()
firstIndex = testWord.find('h')
lastIndex = testWord.rfind('h')
print('First Index: ' + str(firstIndex) + 'Last Index: ' + str(lastIndex))

finalWord = testWord[:firstIndex] + testWord[lastIndex+1::]
print(finalWord)