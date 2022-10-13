# Hacer el diagrama de flujo y el programa en python que averigue e imprima cuantos multiplos de 7 y cuantos multiplos de 9 hay en los numeros comprenedidos entre el 1000 y el 5000

print("\n----------------------------------------------------")
print("-------- Multiplos de 7 y 9 del 1000 al 5000 ------")
print("----------------------------------------------------\n")

m7=0
m9=0

#processing
for i in range(1000,5001):
    if i%7==0:
        m7=m7+1
    if i%9==0:
        m9=m9+1
print(i)

print("\nEntre 1000 y 5000 hay: "+str(m7)+" multiplos de 7")
print("Entre 1000 y 5000 hay: "+str(m9)+" multiplos de 9\n")