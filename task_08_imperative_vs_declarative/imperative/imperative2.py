numbers = [3, 4, 7, 10, 12, 15]

labels = []

for n in numbers:
    if n % 2 == 0 and n < 10:
        labels.append("SMALL_EVEN")
    elif n % 2 == 0 and n >= 10:
        labels.append("LARGE_EVEN")
    else:
        labels.append("ODD")