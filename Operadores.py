#Contamos con adicion +, subtraccion -, multipli *, divi /
#Integer division //, exponenciacion ** y modulo o resuido %
op1=int( input("Escribe un numero: "))
op2=int( input("Escribe un numero: "))
suma=op1+op2
print("Resultado de la suma es: ",suma)
print(f'Resultado de la suma es: {suma}')

resta=op1-op2
print(f'Resultado de la resta es: {resta}')

multi=op1*op2
print(f'Resultado de la multiplicacion es: {multi}')

div=op1/op2
print(f'Resultado de la division es: {div}')
#Esto lo que hace es que solo regresa la parte entera
div=op1//op2
print(f'Resultado de la division es: {div}')

modulo=op1%op2
print(f'Resultado de la modulo es: {modulo}')

exponente=op1**op2
print(f'Resultado de la exponenciacion es: {exponente}')
