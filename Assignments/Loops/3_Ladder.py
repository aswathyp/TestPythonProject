
# Print a Ladder of n steps

# n = int(input('Enter number of ladder steps <= 9: '))

# if n <= 9:
#     k = int(input('Enter kth step < n: '))
#     print('Ladder Steps with Integers: ')
#
#     for i in range(0, n):
#         if i == k:
#             for k in range(1, k+1):
#                 print(k, end='')
#             print(end='\n')
#         else:
#             for j in range(0, i):
#                 print(end=" ")
#             print(i, end='\n')
# else:
#     print('Entered ladder step is greater than 9')

# Solution
ladder = ""
n = int(input('Enter steps of ladder: '))
for i in range(n):
     ladder += str(i+1)
     print(ladder)