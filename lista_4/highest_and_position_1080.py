i = 0;

index = 0
highest = -999999
while i < 2:
    x = int(input())
    if (x > highest):
        index = i
        highest = x

    i += 1

print(highest)
print(index + 1)