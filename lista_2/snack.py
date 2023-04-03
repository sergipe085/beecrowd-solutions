snacks = [4.00, 4.50, 5.00, 2.00, 1.50]
values = input().split(" ")

total = snacks[int(values[0]) - 1] * int(values[1])

print(f"Total: R$ {total:.2f}")