i = 0
odd = 0
even = 0
positive = 0
negative = 0
while i < 5:
    x = int(input())
    if (x > 0):
        positive += 1
    elif (x < 0):
        negative += 1

    if (x % 2 == 0): 
        even += 1
    else:
        odd += 1
    i += 1

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")