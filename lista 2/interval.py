def checkInterval():
    val = float(input())
    interval = 0.0

    while interval <= 75:
        
        if (val >= interval and val <= interval + 25):
            leftBracket = "[" if float(f"{interval:.1f}") == 0.0 else "("
            rightBracket = "]"

            print(f"Intervalo {leftBracket}{int(interval)},{int(interval+25)}{rightBracket}")

            return


        interval += 25

    print("Fora de intervalo")

checkInterval()