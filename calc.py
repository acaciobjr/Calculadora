def calculator(numero1, numero2):
    numero3 = int
    operation = (input(' digite a operação que você deseja realizar: \n'
                              '+, se soma \n'
                              '-, se subtração \n'
                              '*, se multiplicação \n'
                              '/, se divisão \n'))

    if operation == '+':
                    print('{} + {} ='.format(numero1, numero2))
                    print(numero1 + numero2) == numero3
                    question()

    elif operation == '-':
                    print('{} - {} ='.format(numero1, numero2))
                    print(numero1 - numero2) == numero3
                    question()

    elif operation == '*':
                    print('{} * {} ='.format(numero1, numero2))
                    print(numero1 * numero2)  == numero3
                    question()

    elif operation == '/':
                    print('{} / {} ='.format(numero1, numero2))
                    print(numero1 / numero2)  == numero3
                    question(numero1, numero2)

    else:
        print('Você não escolheu um operador válido. Tente novamente.')
        calculator(numero1, numero2)

def question():
    pergunta = input("Deseja fazer outra operação? S para sim qualquer tecla para nâo")
    if pergunta == 'S' or pergunta == 's' :
        numero1 = int(input('Digite o primeiro numero: '))
        numero2 = int(input('Digite o segundo numero: '))
        calculator(numero1, numero2)

    quit()

def main():
    print('### Calculadora em python ###')
    numero1 = int(input('Digite o primeiro numero: '))
    numero2 = int(input('Digite o segundo numero: '))
    calculator(numero1, numero2)

if __name__ == "__main__":
    main()
