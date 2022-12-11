def f(x,n):
    def Factorial(n):
        if n < 1:
            return 1
        else:
            return n * Factorial(n-1)
    return x**n/Factorial(n)
print(f(5,2))