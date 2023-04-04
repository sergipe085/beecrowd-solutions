a, b = map(int, input().split(" "))
while a != b:
    if (a > b):
        print("Decrescente")
    else:
        print("Crescente")
    a, b = map(int, input().split(" "))