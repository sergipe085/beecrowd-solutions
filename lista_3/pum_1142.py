n = int(input())

i = 0;
while i < n:
    j = i * 4
    while j < (i * 4) + 4:
        j += 1;
        if (j == (i * 4) + 4):
            print("PUM", end="")
        else:
            print(j, end=" ")
    print()
    i += 1