n = int(input())
i = 0;
while i < n:
    i+=1
    X = int(input())
    if (X == 0):
        print("NULL")
        continue;
    
    r = "";
    if (X % 2 == 0):
        r += "EVEN "
    else:
        r += "ODD "

    if (X > 0):
        r += "POSITIVE"
    else:
        r += "NEGATIVE"

    print(r)
