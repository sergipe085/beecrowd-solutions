import math

A, B, C = map(float, input().split(" "))

if (A > math.fabs(B - C) and A < B + C):
    print(f"Perimetro = {(A + B + C):.1f}")
else:
    print(f"Area = {((A + B) * C / 2):.1f}")