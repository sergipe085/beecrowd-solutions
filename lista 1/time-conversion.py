time = int(input())

hours = time // (60**2);
minutes = time // 60;
minutes -= hours * 60;
seconds = time;
seconds -= minutes * 60 + hours * 60**2

print(f"{hours}:{minutes}:{seconds}")