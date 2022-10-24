f=list()
while True:
 nome=str(input("Nome: "))
 nota1=float(input("Nota 1: "))
 nota2=float(input("Nota 2: "))
 media=nota1+nota2/2
 f.append([nome,[nota1,nota2],media])
 resp=str(input("Deseja Continuar? [S/N]")).strip().upper()[0]
 if resp in "Nn":
  break
 print(f'{"Nº.":<4}{"NOME":<10}{"MEDIA":>8}')
 for i,a in enumerate(f):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
 opc=int(input("Mostrar nota de qual aluno? [Digite999 para parar]"))
 if opc ==999:
  print("Finalizado")
  break
 if opc<= len(f)-1:
  print(f'Notas de {f[opc] [0]} são {f[opc] [1]}')
print("Finalizado.")