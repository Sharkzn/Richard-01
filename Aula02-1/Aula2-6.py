Idade = 19
Money = 50020
Carro = 50000
if(Idade >= 18 and Money >= 50000):
    print("Carro Aprovado!")
else:
    print("Carro Não Aprovado!")
Sobra = (Money - Carro)
print("Sobrou: " + "R$" + str(Sobra) + " Reais")