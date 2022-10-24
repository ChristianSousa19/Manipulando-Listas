matriz=[0,0,0],[0,0,0],[0,0,0]
somap=somat=maior=0
for l in range(0,3):
  for c in range(0,3):
    matriz[l] [c]=int(input(f"Digite um valor para [{l},{c}]: "))
    if matriz[l] [c]%2==0:
      somap+=matriz[l][c]

print(matriz)
print(f"A soma dos valores pares da matriz é igual a :{somap}")
for l in range(0,3):
  somat+=matriz[l][2]
print(f"A soma dos valores da 3 coluna é igual a :{somat}")
for c in range(0,3):
  if c==0:
    maior=matriz[1][c]
  elif matriz[1][c]>maior:
    maior=matriz[1][c]
print(f"O maior valor da segunda linha é:  {maior}")



