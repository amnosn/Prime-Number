def is_prime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True


number = 110
print(is_prime(number))
