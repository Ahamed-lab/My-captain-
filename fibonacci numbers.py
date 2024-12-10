
def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]


    fib_sequence = [0, 1]
    for i in range(2, n):
        # Add the sum of the last two numbers to the sequence
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence



num_terms = int(input("Enter the number of terms: "))


result = fibonacci(num_terms)
print(f"Fibonacci sequence for {num_terms} terms: {result}")