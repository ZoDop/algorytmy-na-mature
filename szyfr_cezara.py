
def cezar(text, key):
    coded = ''
    for i in text:
        if ord(i) == 32:
            coded += ' '
        else:
            coded += chr((ord(i) - 97 + key) % 26 + 97)
    return coded

print(cezar('abcd zefa', 1))