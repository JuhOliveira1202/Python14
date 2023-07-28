#Exercício 17:
#Receba um número e calcule o fatorial desse numero
#por defeito 0!=1
#n! = 1*2*3*...*(n-1)*n

valor = int(input("introduza o factorial calcular"))

if valor>=0:
    resultado=1
    for i in range(1, valor+1):
        resultado *=i

print("fatorial de, ", valor, "! =!", resultado)
