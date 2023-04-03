from math import copysign as sign

a, b = map(int, input().split(" "))
a_s, b_s = int(sign(1, a)), int(sign(1, b))

mapper = {
    "1 1": "primeiro",
    "-1 1": "segundo",
    "-1 -1": "terceiro",
    "1 -1": "quarto",
}

while (a != 0 and b != 0):
    print(mapper[f"{a_s} {b_s}"])
    a, b = map(int, input().split(" "))
    a_s, b_s = int(sign(1, a)), int(sign(1, b))