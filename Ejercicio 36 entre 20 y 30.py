edad=int(input("Ingrese la edad: "))
venites = edad>=20 and edad<30
print(venites)
treintas = edad>=30 and edad<=40
print(treintas)
'''
if venites or treintas:
    print("Dentro de los rangos 20 y 30")
    if venites :
        print("Dentro de los 20")

    elif treintas:
        print("Dentro de los 30")
else: print("Fuera de los rangos")
'''
if edad>=20 and edad <30 or edad>=30 and edad<=40:
    print("Esta en el rango de los 20 y 30")
else: print("Esta en el rango de los 40 o mas")


#Mejora de código
if (20<= edad <30) or (30 <= edad <40):
    print("Esta en el rango de los 20 y 30")
else: print("Tienes 40 o más años")
