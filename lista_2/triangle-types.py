def main():

  sides = input().split(" ")
  a = []
  for i in sides:
    a.append(float(i))
  a.sort(reverse=True)

  A = float(a[0])
  B = float(a[1])
  C = float(a[2])

  if A >= (B + C): 
    print("NAO FORMA TRIANGULO")
    return
  if A**2 == B**2 + C**2: print("TRIANGULO RETANGULO")
  if A**2 > B**2 + C**2: print("TRIANGULO OBTUSANGULO")
  if A**2 < B**2 + C**2: print("TRIANGULO ACUTANGULO")
  if A == B and B == C: print("TRIANGULO EQUILATERO")
  if (A == B and A != C) or (B == C and B != A) or (C == A and A != B): print("TRIANGULO ISOSCELES")

main()