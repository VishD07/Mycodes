def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b

n = int(input("Enter a number: "))
fibonacci(n)
