
def is_perfect(number):
    if number <= 1:
        return False

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    return total == number
