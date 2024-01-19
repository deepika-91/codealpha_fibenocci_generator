def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
n = input("Enter how many fibonacci series to be generated: ")
n=int(n);
fibonacci_sequence = []
generator = fibonacci_generator()

for _ in range(n):
    fibonacci_sequence.append(next(generator))

print(f"Fibonacci sequence of the first {n} numbers:")
print(f"{fibonacci_sequence}")