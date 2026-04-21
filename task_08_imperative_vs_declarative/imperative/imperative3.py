numbers = [2, 3, 5, 6, 9, 10, 12, 15, 18, 20]

labels = []

for n in numbers:
    if n % 3 == 0  and n % 2 == 0:
        labels.append("CRITICAL")
    elif n % 3 == 0 and n % 2 != 0:
        labels.append("IMPORTANT")
    elif n % 2 == 0 and n >= 10:
        labels.append("SECONDARY")
    else:      
        labels.append("NORMAL")
print(labels)