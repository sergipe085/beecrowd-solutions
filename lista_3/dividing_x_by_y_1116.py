n = int(input())
i = 0;
while i < n:
    i+=1
    x, y = map(float, input().split(" "))
    if (y == 0):
        print("divisao impossivel")
        continue
    print(f"{x/y:.1f}")