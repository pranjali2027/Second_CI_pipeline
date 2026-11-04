def most_frequent(numbers):
    if not numbers:
        return None

    frequency = {}

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    return max(frequency, key=frequency.get)