valor1= float(input('Digite o primeiro valor da operacao'))
valor2= float(input('Digite o segundo valor da operacao'))
operacao= int(input('Escolha operacao aritmetica ( 1- +,2- -,3- *,4- /) '))
if operacao==1:
    soma=valor1+valor2
    print('O valor da soma é', soma)
elif operacao==2:
    subtracao=valor1-valor2
    print('O valor da subtracao é', subtracao)
elif operacao==3:
    multiplicacao=valor1*valor2
    print('O valor da multiplicacao é', multiplicacao)
elif operacao==4:
    divisao=valor1/valor2
    print('O valor da divisao é', divisao)
else:
    print('Escolha o numero corrento referente a operacao')