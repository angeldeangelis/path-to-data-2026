words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else: and for now, comment out the print with the call to pin_extractor.
        print(f"'{word}' has no vowels")

numbers = [141545, 22131245, 31525, 45124, 55123123]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    if number % 5 == 0:
        print(f"{number} is a multiple of 5")
    else:
        print(f"{number} is not a multiple of 5")
    for digits in str(number):
        if digits == '1':
            print(f"{number} contains the digit '1'")
            break
    else:
            print(f"{number} does not contain the digit '1'")
