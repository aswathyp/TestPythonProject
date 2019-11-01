#access using nested loops
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

#acess using elements (not indices)
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

a=[0]*10
#[0,0,0,0,0,0,0,0]

n = 4
m = 4
a=[]
# a.p
a = [[0] * m] * n
a[0][2]=10
print("TWO D ZEROs")
print(a)

#propoer using list*n
n = 3
m = 4
a = [0] * m

for i in range(n):
    a[i] = [0] * m

a[0][0] = 5
print("Correct two d  create")
print(a[1][0])

#proper
n = 3
m = 4
a = []
for i in range(n):
    a.append([0] * m)

#best easy way
n = 3
m = 4
a = [[0] * m for i in range(n)]

#inout to twoD
print("READING LIST")
n = int(input())
a = []
for i in range(n):
    print("READING ", i,"th", "row")
    a.append([int(j) for j in input().split()])


#best way using generators
n = int(input())
a = [[int(j) for j in input.split()] for i in range(n)]