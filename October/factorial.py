def factorial(n):
    result = 1
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0: 
        return 1
    for i in range(1, n + 1):
        result *= i
    return result