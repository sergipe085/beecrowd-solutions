values = input().split(" ")

sh = int(values[0])
eh = int(values[1])

start = sh;
end = eh;

time = 0
if (end <= start):
    time = 24  - (start - end)
else:
    time = end - start

print(f"O JOGO DUROU {time} HORA(S)")