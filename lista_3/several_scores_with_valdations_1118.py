def calcular_media():
    a = float(input());
    while a < 0 or a > 10:
        print("nota invalida")
        a = float(input())    

    b = float(input());
    while b < 0 or b > 10:
        print("nota invalida")
        b = float(input())

    print(f"media = {(a + b)/2:.2f}")

def novo_calculo():
    print("novo calculo (1-sim 2-nao)")
    X = int(input())
    while(X != 1 and X != 2):
        print("novo calculo (1-sim 2-nao)")
        X = int(input())
    return X

calcular_media()

x = novo_calculo()

while x != 2:
    calcular_media()
    x = novo_calculo()

