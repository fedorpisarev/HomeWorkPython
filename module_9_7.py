def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, int(result * 0.5) + 1):
            if result % i == 0 or result < 2:
                print("Составное")
                break
        else:
            print("Простое")
        return result
    return wrapper



@is_prime
def sum_three(a,b,c):
    res = a + b + c
    return res



result = sum_three(2, 3, 6)

print(result)
