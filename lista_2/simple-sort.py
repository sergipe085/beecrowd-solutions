valores = list(map(int, input().split(" ")))

def my_sort(a):
    if (len(a) <= 1):
        return a;

    menores = []
    maiores = []
    pivo = [a[0]]
    for i in a:
        if (i < pivo[0]):
            menores.append(i)
        elif (i > pivo[0]):
            maiores.append(i)
            
    return my_sort(menores) + pivo + my_sort(maiores)

for i in my_sort(valores):
    print(i)
print()
for i in valores:
    print(i)
    