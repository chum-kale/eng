def fibonacci(n, steps=0):
    if n <= 0:
        return (0, steps)
    elif n == 1:
        return (1, steps)
    else:
        steps += 1
        fib1, _ = fibonacci(n - 1, steps)
        fib2, _ = fibonacci(n - 2, steps)
        return (fib1 + fib2, steps)

n = int(input("Enter the value of n: "))
fibonacci_number, step_count = fibonacci(n)
print(f"The {n}-th Fibonacci number is {fibonacci_number}")
print(f"Step count: {step_count}")
