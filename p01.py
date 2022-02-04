# Haga un programa en Python que lea los tres lados de un triangulo
# y diga que clase de triangulo es
# Equilatero 3 lados iguales
# isóceles 2 lados iguales
# Escaleno si todos los lados son diferentes

l1=float(input('Digite el primer lado: '))
l2=float(input('Digite el segundo lado: '))
l3=float(input('Digite el tercer lado: '))

if(l1==l2 and l2==l3 and l1==l3):
    print('Es Equilatero')

else:
    if(l1!=l2 and l2!=l3 and l1!=l3):
        print('Es Escaleno')
    else:
        print('Es isósceles')
    #end if
#end if


