#Fibonacci Series

series = int(input('Enter # of Fibonacci Series: '))
fibonacciSeries=[0, 1]
count = 3

def fibonacci(x, y, count):
    z = x + y
    x = y
    y = z
    fibonacciSeries.append(z)

    if count < series:
        count+=1
        fibonacci(x, y, count)

fibonacci(0, 1, count)
print(fibonacciSeries)