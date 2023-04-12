n = int(input())

i = 0;
in_c = 0
while i < n:
    x = int(input())

    if (10 <= x <= 20):
        in_c += 1
         
    i+=1

out_c = n - in_c

print(in_c, "in")
print(out_c, "out")
