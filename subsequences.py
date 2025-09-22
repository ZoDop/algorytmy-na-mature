
# najdluzszy podciag z liczb pazrystych
file = open('subaequences.txt', 'r')

max_len = 0
max_row = 0
len = 0
row = 0
current_row = 1
for line in file:
    line.strip().split()
    number = int(line)
    if number % 2 == 0 and len == 0:
        row = current_row
        len = 1
        if len > max_len:
            max_len = len
            max_row = row
    elif number % 2 == 0 and len != 0:
        len += 1
        if len > max_len:
            max_len = len
            max_row = row
    else:
        len = 0

    current_row += 1

print(max_row)
print(max_len)








# najdluzszy podciag nierosnacy
file = open('subaequences.txt', 'r')

max_len = 0
max_row = 0
len = 0
row = 0
current_row = 1
for line in file:
    line.strip().split()
    number = int(line)
    if current_row == 1:
        row = current_row
        max_len += 1
        len += 1







