x = int(input());
y = int(input());

if (x > y):
    x,y = y,x

i = x + 1
total = 0
while i < y:
    if (i % 2 == 1):
        total += i
    i+=1

print(total)
