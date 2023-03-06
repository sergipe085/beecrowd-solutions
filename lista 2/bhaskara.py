import math

def main():
    A, B, C = map(float, input().split(" "))

    if (A <= 0):
        print("Impossivel calcular")
        return;

    delta = B*B - (4 * A * C);

    print(delta);
    print(math.sqrt(delta))

    if (delta < 0):
        print("Impossivel calcular")
        return
    
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)
    
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")

main()