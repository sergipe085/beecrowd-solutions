values = input().split(" ")

sh = int(values[0])
sm = int(values[1])
eh = int(values[2])
em = int(values[3])

start = sh * 60 + sm;
end = eh * 60 + em;

time = 0
if (end <= start):
    time = 24 * 60  - (start - end)
else:
    time = end - start

print(f"O JOGO DUROU {time // 60} HORA(S) E {time % 60} MINUTO(S)")