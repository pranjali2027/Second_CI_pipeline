def missing_number(numbers):
    n = len(numbers)
    result = 0

    for i in range(n + 1):
        result ^= i

    for num in numbers:
        result ^= num

    return result