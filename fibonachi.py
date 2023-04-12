n = int(input("Digite a quantidade de termos: "))

t1 = int(input("Digite o primeiro numero: "))
t2 = int(input("Digite o segundo numero: "))

def fibonachi(a, b, n, i = 0):

    print(a + b, end=" ");

    s = a + b

    if (i >= n):
        return s
    

    return fibonachi(b, s, n, i + 1)

fibonachi(t1, t2, n)