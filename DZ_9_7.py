def is_prime(func):
    def wrapper(*args, **kwargs):
    #def wrapper():
        original_result = func(*args, **kwargs)
        count = 0
        for i in range(1, original_result+1):
            if original_result % i == 0:
                if i == 1 or i == original_result:
                    count += 1
                else:
                    count += 1
        if count == 2:
            print(f'Простое число')
        else:
            print(f'Составное число')

        return original_result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 3, 6))

