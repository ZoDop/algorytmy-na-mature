
def cezar(text, key):
    coded = ''
    for i in text:
        if ord(i) == 32:
            coded += ' '
        else:
            coded += chr((ord(i) - 97 + key) % 26 + 97)
    return coded


print(cezar('abcd zefa', 1))



def szyfruj(slowo, klucz):
    zaszyfrowane_slowo = ""
    for i in range(len(slowo)):
            klucz = klucz % 26
            znak = chr(ord(slowo[i]) + klucz)
            if znak > 'z':         # przypadek w którym znak wyszedł poza alfabet
                znak = chr(ord(znak) - 26)
            zaszyfrowane_slowo += znak
    return zaszyfrowane_slowo


    def odszyfruj(slowo, klucz):
    odszyfrowane_slowo = ""
    for i in range(len(slowo)):
            klucz = klucz % 26
            znak = chr(ord(slowo[i]) - klucz)
            if znak < 'a':         # przypadek w którym znak wyszedł poza alfabet
                znak = chr(ord(znak) + 26)
            odszyfrowane_slowo += znak
    return odszyfrowane_slowo
