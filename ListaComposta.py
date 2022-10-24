prin=list()
lista=list()
r=" "
pessoas=0
maiorp=0
menorp=0
while True:
    lista.append(float(input("Digite seu peso kg: ")))
    lista.append(input("Digite seu nome: "))
    pessoas+=1
    if len(prin)==0:
        maiorp=menorp=lista[0]
    else:
        if lista[0]>maiorp:
            maiorp=lista[0]
        if lista[0]<menorp:
            menorp=lista[0]
    prin.append(lista[:])
    lista.clear()
    w = str = input("Deseja continuar? [S/N]").strip().upper()[0]
    if w in "Nn":
        break
print(f"Ao total temos {pessoas} pessoas cadastradas : ")
print(f"{maiorp}kg foi o maior peso registrado, respectivamente de ",end="" )
for p in prin:
    if p[0]==maiorp:
        print(f"[{p[1]}]",end=" ")
print(f"e {menorp}kg foi o menor peso registrado,respectivamente de ",end="")
for p in prin:
    if p[0]==menorp:
        print(f"[{p[1]}]",end=" ")