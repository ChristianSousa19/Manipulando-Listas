import random
import time
jogos=list()
lista=list()
cont=0
quanto=int(input("Quantos jogos deseja sortear?"))
total=1
while total<=quanto:
    cont=0
    while True:
     num=random.randint(1,60)
     if num not in lista:
        lista.append(num)
        cont+=1
     if cont>6:
        break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total+=1
print(f"Os numeros sorteados foram {lista}")
for i,l in enumerate(jogos):
    print(f"Jogo{i+1}:{l}")
    time.sleep(1)