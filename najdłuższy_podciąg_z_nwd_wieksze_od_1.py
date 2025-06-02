
# najdłuższy podciąg w tablicy 2d z NWD wiekszym od 1 poziomo albo pionowo


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

file = open("tablica_2d_podciągi.txt", "r")
tablica = []
for line in file:
    tablica.append(line.split())