num =int( input("Proporciona un valor de 1 y 3: "))

if num == 1:
    numerotex= 'Número uno'
elif num== 2:
    numerotex= 'Núumero Dos'
elif num == 3:
    numerotex= 'Número tres'
else:
    print("Valores fuera de rango")

print(f'Número proporcionado {num} - {numerotex}')