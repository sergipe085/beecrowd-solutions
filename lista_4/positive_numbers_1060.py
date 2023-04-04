i = 0
c = 0
while i < 6:
    x_string = input()
    if (x_string.isnumeric()):
        x = int(x_string)
        if (x > 0):
            c += 1
    i += 1

print(f"{c} valores positivos")