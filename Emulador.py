velocidade_permitida = float(input("Digite a velocidade permitida na via:"))
velocidade_registrada = float(input("Digite a velocidade registrada pelo radar:"))

excesso = velocidade_registrada - velocidade_permitida

if excesso <= 0:
    print("Motorista dentro do limite!")
else:
    porcentagem_excedida = (excesso / velocidade_permitida ) * 100

    if porcentagem_excedida > 20 :
        print(f"Infração Média \nPorcentagem excedida: {porcentagem_excedida}% \nMulta no valor de R$ {130.16*(porcentagem_excedida/100):.2f}")
        
    elif porcentagem_excedida >= 50 :
        print(f"Infração Grave! \nPorcentagem excedida: {porcentagem_excedida}% \nMulta no valor de R$ {195.23*(porcentagem_excedida/100):.2f}")

    else:
        print(f"Infração Gravíssima!! \nPorcentagem excedida: {porcentagem_excedida}% \nMulta no valor de R$ {(293.47*(porcentagem_excedida/100)*3):.2f}")