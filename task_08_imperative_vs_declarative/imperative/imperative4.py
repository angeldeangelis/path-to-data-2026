numbers = [4, 6, 8, 9, 10, 12, 15, 16, 18, 21, 24]

labels = []

for n in numbers:

    if (n % 2 == 0 and n % 4 == 0) and (n % 3 == 0):
        labels.append("CRITICAL")

    elif (n % 3 == 0) and (n % 2 != 0):
        labels.append("IMPORTANT")

    elif (n % 2 == 0) and not (n % 4 == 0):
        labels.append("SECONDARY")

    else:
        labels.append("NORMAL")


for n, label in zip(numbers, labels):
    print(n, "→", label)