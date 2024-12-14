def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % result == 0 and result != 0:
            print('простое')
        return result
    return wrapper



@is_prime
def sum_three(a,b,c):
    res = a + b + c
    return res



result = sum_three(2, 3, 6)
print(result)