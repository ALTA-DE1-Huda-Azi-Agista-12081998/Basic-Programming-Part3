def full_prima(N):
    # your code here
    def is_prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, n))

    for digit_str in str(N):
        digit = int(digit_str)
        if not is_prime(digit):
            return False
    return True
    

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True