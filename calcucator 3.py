from logging import shutdown


def soma(x, y):
    return x + y


def subtraçao(x, y):
    return x - y


def divisao(x, y):
    return x / y


def multiplicaçao(x, y):
    return x * y

history = []

def calculadora():
    num1 = (input('digite o  primeiro numero: '))
    try:
        val = float(num1)
        print('valid number')
    except ValueError:
     print('invalid number')
     calculadora()

    a = input('indicate your sinal: +, -, /, *, :')

    num2 = (input('digite o  segundo numero: '))
    try:
        val = float(num2)
        print('valid number')
    except ValueError:
        print('invalid number')
        calculadora()

    if a == '+':
        result = soma(float(num1), float(num2))
        print('resultado de soma: ' + str(result))
        history.insert(0, result)

    if a == '-':
        result1 = subtraçao(int(num1), int(num2))
        print('resultado de subtraçao: ' + str(result1))
        history.insert(0, result1)

    if a == '/':
        result2 = divisao(int(num1), int(num2))
        print('resultado de divisao: ' + str(result2))
        history.insert(0, result2)

    if a == '*':
        result3 = multiplicaçao(int(num1), int(num2))
        print('resultado de multiplicaçao: ' + str(result3))
        history.insert(0, result3)

    if a != '+' and a != '-' and a != '*' and a != '/':
        print('!!!!!!try again, the problem in +, -, *, or /...')
        calculadora()
    else: pass

    if len(history) >= 6:
        history.pop(5)

    e = input("show history? yes/no: ")
    if e == 'yes' or e == 'Yes' or e == 'YES':
        print(list(history))
    else:
        pass



    b = input("stop? yes/no: ")
    if b == 'yes' or b == 'Yes' or b == 'YES':
        shutdown()
    else:
        calculadora()


calculadora()
