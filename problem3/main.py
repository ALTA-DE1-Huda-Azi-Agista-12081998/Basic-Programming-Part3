def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

print(prime_number(7))  # True
print(prime_number(10)) # False
print(prime_number(11)) # True
print(prime_number(13)) # True
print(prime_number(17)) # True
print(prime_number(20)) # False
print(prime_number(35)) # False
