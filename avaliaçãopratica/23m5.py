a=float(input('Digite o comprimento da reta a'))
b=float(input('Digite o comprimento da reta b'))
c=float(input('Digite o comprimento da reta c'))
if c>b+a or b>a+c or a>c+b:
    print ('Nao é um triangulo')
elif a==b and b==c and c==a:
    print('triagulo equilátero')
elif a==b or b==c or a==c:
    print('triangulo isoceles')
else:
    print('triangulo escaleno')
