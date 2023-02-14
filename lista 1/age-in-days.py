days = int(input())

ano = days // 365;
days -= 365 * ano;
mes = days // 30;
days -= 30 * mes;

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{days} dia(s)")