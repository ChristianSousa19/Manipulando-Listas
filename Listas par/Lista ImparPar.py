lista=list(),list()
for i in range(1,8):
    p=int(input("Digite um valor: "))
    if p%2==0:
        lista[0].append(p)
    if p%2==1:
        lista[1].append(p)
print(f"Os numeros pares foram {sorted(lista[0])}")
print(f"Os numeros impares foram {sorted(lista[1])}")
