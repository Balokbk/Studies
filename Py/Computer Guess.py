from random import randint

def chuteComputador(num:int):
    tentativasFalhas = set()
    numTentativas = 0
    min = 1
    if num > 1000:
        max = num + 100
    else:
        max = 1000
    chute = randint(min,max)

    while True:
        if chute == num:
            break
        if chute in tentativasFalhas:
            chute = randint(min,max)
        else:
            tentativasFalhas.add(chute)
            print(f"O chute foi de: {chute}")
            numTentativas += 1
            chute = randint(min,max)
    if chute == num:
        print(f"\nFoi necessárias {numTentativas} tentativas para chegar no número!\n")

def numeroInp():
    try:
        numero = int(input("Insira um número acima de 1 para o computador adivinhar: "))
        if numero < 1:
            print("Digite um número acima de 1")
            numeroInp()
        else:
            chuteComputador(numero)

    except ValueError:
        print("Insira um número válido")
        numeroInp()

numeroInp()