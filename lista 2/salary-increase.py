salary = float(input())

increaseRate = 1.04

if (0.0 <= salary <= 400.0):
    increaseRate = 1.15
elif (400.0 < salary <= 800.0):
    increaseRate = 1.12
elif (800.0 < salary <= 1200.0):
    increaseRate = 1.1
elif (1200.0 < salary <= 2000.0):
    increaseRate = 1.07

newSalary = salary * increaseRate
reajuste = newSalary - salary
percentual = (increaseRate - 1.0) * 100.0

print(f"Novo salario: {newSalary:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual:.0f} %")
