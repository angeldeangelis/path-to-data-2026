numbers = [1, 2, 3, 4, 5, 6]

is_even = []

for n in numbers:
    if n % 2 == 0:
        is_even.append(True)
    else:
        is_even.append(False)

print(is_even)