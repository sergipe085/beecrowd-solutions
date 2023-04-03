def main():
    X, Y = map(float, input().split(" "))
    X = my_sign(X)
    Y = my_sign(Y)

    if (X == 0 and Y == 0):
        print("Origem")
        return
    
    if (X + Y == 1 or X + Y == -1):
        print(f"Eixo {'X' if X != 0 else 'Y'}")

    i = 1
    x = 1
    y = 1
    while i <= 4:    
        if (X == x and Y == y):
            print(f"Q{i}")
            break

        if (i % 2 == 1):
            x *= -1
        else:
            y *= -1
        
        i += 1

def my_sign(x):
    return (x > 0) - (x < 0)

main()