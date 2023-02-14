value = int(input())
i = 10
print(value)
while i >= 0.1:
    target = int(i * 10)
    notes = value // target
    value -= notes * target
    print(f"{notes} nota(s) de R$ {target},00")
    if i > 1 :
        i = i // 2
    else:
        i = i / 2