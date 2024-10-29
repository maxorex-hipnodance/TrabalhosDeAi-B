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
    num1 = (input('Insert first number: '))
    try:
        val = float(num1)
    except ValueError:
     print('invalid number')
     calculadora()

    a = input('Indicate your sinal: +, -, /, *, : ')

    num2 = (input('Insert second number: '))
    try:
        val = float(num2)
    except ValueError:
        print('invalid number')
        calculadora()

    if a == '+':
        result = soma(float(num1), float(num2))
        print('Result of amount: ' + str(result))
        history.insert(0,result)

    if a == '-':
        result1 = subtraçao(float(num1), float(num2))
        print('Result of subtraction: ' + str(result1))
        history.insert(0, result1)

    if a == '/':
        result2 = divisao(float(num1), float(num2))
        print('Result of division: ' + str(result2))
        history.insert(0, result2)

    if a == '*':
        result3 = multiplicaçao(float(num1), float(num2))
        print('Result of multiplication: ' + str(result3))
        history.insert(0, result3)

    if a != '+' and a != '-' and a != '*' and a != '/':
        print(' !ALER!try again The problem in +, -, *, or / ... ')
        calculadora()
    else: pass

    if len(history) >= 6:
        history.pop(5)

    e = input("Show history? yes/no: ")
    if e == 'yes' or e == 'Yes' or e == 'YES':
        print(record)
    else:
        pass



    b = input("Stop? yes/no: ")
    if b == 'yes' or b == 'Yes' or b == 'YES':
        shutdown()
    else:
        calculadora()


calculadora()