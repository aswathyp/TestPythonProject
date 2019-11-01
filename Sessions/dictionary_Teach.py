
#Data structure, which allows to use an arbitrary type of index
# instead of numerical, is called dictionary or associative array.
# The corresponding data structure in Python is called dict.
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
#Capitals = dict(RA = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
print(Capitals)
Capitals = dict([("Russia", ["Moscow","million",1]), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))

myDict= dict(zip("SATISH","12345"))
print(Capitals)
#Keys handling
A = {'ab' : 'ba', 'aa' : 'aa', 'bb' : 'bb', 'ba' : 'ab'}


key = 'ac'
if key in A:
    del A[key]

try:
    del A[key]
except KeyError:
	print('There is no element with key "' + key + '" in dict')
print(A)

#keys, values iteration
A = dict(zip('abcdef', list(range(6))))
for key, val in A.items():
    print(key, val)


a={}
a["satish"]=25
a["ganesh"]=15

a.items()

k="satish"
print(k, a[k])
print(a)
a.keys()


