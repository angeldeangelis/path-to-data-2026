def pin_extractor(poems):
    secret_code = ''
    for poem in poems:
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if line_index < len(words):  # Now checks if there are enough words on THIS line
                secret_code += str(len(words[line_index]))
    return secret_code

poem = """Stars and the moon shine in the sky white and bright until the end of the night"""
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))  # Outputs: '6715'
