import random

def cria():
    lista = []
    naipes = '♣♥♠♦'
    i = 0
    while i < len(naipes):
        for valor in range(1, 14):    
            c = (valor, naipes[i])
            lista.append(c)
        i = i + 1

    #lista.append(0, 'joker')
    #lista.append('joker', 'joker')
    return lista

def compra(baralho: list):
    return baralho.pop()

def distribui(baralho: list, qtd: int):
    mao = []
    i = 0
    while i < qtd:
        c = compra(baralho)
        mao.append(c)
        i = i + 1
    return mao    

def embaralha(baralho: list):
    for vezes in range(300):
        i = random.randint(0, len(baralho) - 1)
        j = random.randint(0, len(baralho) - 1)
        aux = baralho[i]
        baralho[i] = baralho[j]
        baralho[j] = aux
