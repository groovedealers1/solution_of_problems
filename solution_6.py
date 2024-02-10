# Count the number of divisors of a positive integer n.

def divisors(n):
    return len([i for i in range(1, n + 1) if n % i == 0])


n = 14
print(divisors(n))