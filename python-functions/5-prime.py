def is_prime(number):
    """Checks if a number is prime"""
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
