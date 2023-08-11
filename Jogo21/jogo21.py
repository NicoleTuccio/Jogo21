import baralho

def soma_pontos(mao: list):
    soma = 0
    for carta in mao:
        if carta[0] < 10:
            soma = soma + carta[0]
        else:
            soma = soma + 10
    return soma

def quer_carta(mao_jog):
    pts = soma_pontos(mao_jog)
    print("MAO: ", mao_jog)
    print("PTS: ", pts)
    resp = input("Quer carta (s/n)?")
    if resp == 's':
        return True
    else:
        return False

def quer_carta_cpu(mao):
    pts = soma_pontos(mao)
    if pts < 16:
        return True
    else:
        return False
    
#PROGRAMA PRINCIPAL (MAIN)
monte = baralho.cria()
baralho.embaralha(monte)

mao_jog = baralho.distribui(monte, 2)
mao_cpu = baralho.distribui(monte, 2)

while quer_carta(mao_jog):
    carta = baralho.compra(monte)
    mao_jog.append(carta)

while quer_carta_cpu(mao_cpu):
    carta = baralho.compra(monte)
    mao_cpu.append(carta)

pts_jog = soma_pontos(mao_jog)
pts_cpu = soma_pontos(mao_cpu)

print("JOG -> ", mao_jog, pts_jog)
print("CPU -> ",mao_cpu, pts_cpu)

if pts_cpu > 21 and pts_jog <= 21:
    print("EU ganhei!")
elif pts_cpu <= 21 and pts_jog > 21:
    print("CPU ganhou!")
elif pts_jog > pts_cpu:
    print("EU ganhei!")
else:
    print("CPU ganhou!")
