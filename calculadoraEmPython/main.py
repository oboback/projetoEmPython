#Calculadora em python
import math

print('''
Bem-vindo a minha calculadora em python!!!
''')

def calcu():
    operacao = input('''
Por favor, escolha uma operação para cotinuar:
Ser for LETRA, por favor inserir em maíuscula!
+ para adiçao
- para subtraçao
* para multiplicaçao
/ para divisao
% para porcentagem
** para exponente
RQ para raiz quadrada
''')

    if operacao == '+':
        primenume = float(input('Coloque seu primeiro número: '))
        segunnume = float(input('Coloque outro número: '))
        print('{} + {} = '.format(primenume, segunnume))
        print(primenume + segunnume)
    elif operacao == '-':
        primenume = float(input('Coloque seu primeiro número: '))
        segunnume = float(input('Coloque outro número: '))
        print('{} - {} = '.format(primenume, segunnume))
        print(primenume - segunnume)
    elif operacao == '*':
        primenume = float(input('Coloque seu primeiro número: '))
        segunnume = float(input('Coloque outro número: '))
        print('{} * {} = '.format(primenume, segunnume))
        print(primenume * segunnume)
    elif operacao == '/':
        primenume = float(input('Coloque seu primeiro número: '))
        segunnume = float(input('Coloque outro número: '))
        if segunnume == 0:
            print('Qualquer número dividido por 0, o resultado é 0!')
        else:
            print('{} / {} = '.format(primenume, segunnume))
            print(primenume / segunnume)
    elif operacao == '%':
        primenume = float(input('Coloque o número da porcentagem: '))
        segunnume = float(input('Coloque o segundo número: '))
        print('{} % {} = '.format(primenume, segunnume))
        print(segunnume * (primenume / 100))
    elif operacao == '**':
        primenume = float(input('Coloque seu primeiro número: '))
        segunnume = float(input('Coloque o exponêncial: '))
        print('{} ** {} = '.format(primenume, segunnume))
        print(primenume ** segunnume)
    elif operacao == 'RQ':
        primenume = float(input('Coloque o número para calcular a raiz: '))
        print('A raiz quadrada de {} é = '.format(primenume))
        print(math.sqrt(primenume))
    else:
        print('você digitou uma operação inválida.')
        calcu()

def novam():
    while True:
        calcu_novam = input('''
        Você quer calcular novamente?
        Por favor escolha S para Sim ou N para Não.
        ''')
        if calcu_novam.strip().upper() == 'S':
            calcu()
        elif calcu_novam.strip().upper() == 'N':
            print('Até mais!')
            break
        else:
            novam()
    
calcu()
novam()