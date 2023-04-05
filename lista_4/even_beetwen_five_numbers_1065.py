i = 0
c = 0
while i < 5:
    x = int(input())
    if (abs(x) % 2 == 0):
        c += 1
    i += 1

print(f"{c} valores pares")