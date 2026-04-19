consumo = float(input("Informe o consumo em m3:"))

if consumo <= 10:
    print(f"O valor da conta de água deste mês ficou R${45 + (consumo * 2.5):.2f}")

elif consumo <= 30:
    print(f"O valor da conta de água deste mês ficou R${45 + 10 * 2.5 + ((consumo - 10) * 4.1):.2f}")

else:
    print(f"O valor da conta de água deste mês ficou R${45 + (10 * 2.5) + (20 * 4.1) + ((consumo - 30) * 7.5):.2f}")