A, B = map(int, input().split(" "))

i = 1
a = 1;
while True:
    a = A * i

    if (A * B == 0 or a == B):
        print("Sao Multiplos")
        break
    if (a > B):
        print("Nao sao Multiplos")
        break

    i += 1