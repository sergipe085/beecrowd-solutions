i = 0
c = 0
total = 0
while i < 6:
    try:
        x = float(input())
        if (x > 0):
            c += 1
            total += x
    except:
        pass
    i += 1

print(f"{c} valores positivos")
print(f"{total/c:.1f}") 