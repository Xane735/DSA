def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def print_fib_series(n):
    print("Fibonacci series:", end=" ")
    for i in range(n):
        print(fib(i), end=" ")
    print()

# Example
n = 10
print_fib_series(n)
