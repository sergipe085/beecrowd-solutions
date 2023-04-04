n = 0b1111000011110000
p = 0
while p < 16:
    print((n & ( 1 << p )) >> p)
    p+=1