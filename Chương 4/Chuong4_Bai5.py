def Fibonacci(n):
    if n <=2:
        return 1
    else:
        return Fibonacci(n -1) + Fibonacci(n-2)
def dsFibonacci(n):
    for i in range(1, n+1, 1):
        print(Fibonacci(i), end='\t')

print(Fibonacci(9))
dsFibonacci(9)