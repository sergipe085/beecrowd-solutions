values = input();

x = values.split(" ")

A = int(x[0])
B = int(x[1])
C = int(x[2])
D = int(x[3])

sumCD = C + D;
sumAB = A + B;
accepted = B > C and D > A and sumCD > sumAB and A % 2 == 0
if (accepted):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")