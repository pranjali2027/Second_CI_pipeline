def move_zeros(numbers):
    non_zeros = []

    for num in numbers:
        if num != 0:
            non_zeros.append(num)

    zeros = [0] * (len(numbers) - len(non_zeros))

    return non_zeros + zeros