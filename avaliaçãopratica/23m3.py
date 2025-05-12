valor1= int(input('Digite valor 1'))
valor2= int(input('Digite valor 2'))
valor3= int(input('Digite valor 3'))
if valor1> valor2 and valor1>valor3:
    print(valor1)
elif valor2> valor1 or valor3:
    print(valor2)
elif valor3>valor2 and valor3>valor1:
    print(valor3)
else:
    print('Empate entre valores')