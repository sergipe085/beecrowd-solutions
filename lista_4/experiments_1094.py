n = int(input())

i = 0
animals = {
    "C": 0,
    "R": 0,
    "S": 0
}

while i < n:
    inp = input().split(" ")
    quantity = int(inp[0])
    animal = inp[1]

    animals[animal] += quantity
    i += 1

total = 0
for t in animals:
    total += int(animals[t])

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {animals['C']}")
print(f"Total de ratos: {animals['R']}")
print(f"Total de sapos: {animals['S']}")
print(f"Percentual de coelhos: {animals['C']*100/total:.2f} %")
print(f"Percentual de ratos: {animals['R']*100/total:.2f} %")
print(f"Percentual de sapos: {animals['S']*100/total:.2f} %")
