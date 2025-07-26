def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def binomial_coefficient(n, k):
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

print(f"Factorial of {n} = {factorial(n)}")
print(f"Binomial Coefficient C({n}, {k}) = {binomial_coefficient(n, k)}")