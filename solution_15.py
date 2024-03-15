def factorial(n):
    b, answer = 1,  [i for i in range(1, n + 1)]
    answer = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            answer *= i
    return answer


num = 5
print(factorial(num))
