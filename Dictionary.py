
# Dictionary

#Associative Array

#Tuple (1,2)
#List of Tuples --> [(1,2),(3,4)]
Capitals = {'Russia': 'Moscow', 'India': 'New Delhi'}

Capitals = dict(RA = 'Moscow', India = 'New Delhi')
Capitals = dict([('India', 'New Delhi'), ('Canada', 'Ottawa'), ('Ukraine', 'Kiev')])
Capitals = dict(zip(['India', 'Canada', 'Ukraine'], ['New Delhi', 'Ottawa', 'Kiev')]))


A = dict(zip('abcdef', list(range(6))))
for key, val in A.items():
    print('Key:', key, sep=' ')
    print('Val:', val, sep=' ')

myDict = dict(zip('Sathish', '123456'))
print('mydict: ', myDict, end='\n')

A = {'ab': 'ba', 'ca': 'ac', 'hi': 'ih'}
print(A)
key = 'ac'
if key in A:
    print('Deleted the key value pair', key, A[key])
    del A[key]
else:
    print('Key not found')

print(A)
print(A.keys())
print(A.items())