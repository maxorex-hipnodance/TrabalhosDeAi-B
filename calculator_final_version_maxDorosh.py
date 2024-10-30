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
    num1 = (input('\nInsert first number: '))
    try:
        val = float(num1)
    except ValueError:
     print('⚠️invalid number⚠️')
     calculadora()

    a = input('\nIndicate your sinal: +, -, /, *, : ')

    num2 = (input('\nInsert second number: '))
    try:
        val = float(num2)
    except ValueError:
        print('⚠️invalid number⚠️')
        calculadora()

    if a == '+':
        result = soma(float(num1), float(num2))
        print('\nResult of amount: ' + str(result))
        history.insert(0,f'{num1} {a} {num2} = {result}')

    if a == '-':
        result1 = subtraçao(float(num1), float(num2))
        print('\nResult of subtraction: ' + str(result1))
        history.insert(0, f'{num1} {a} {num2} = {result1}')

    if a == '/':
        result2 = divisao(float(num1), float(num2))
        print('\nResult of division: ' + str(result2))
        history.insert(0, f'{num1} {a} {num2} = {result2}')

    if a == '*':
        result3 = multiplicaçao(float(num1), float(num2))
        print('\nResult of multiplication: ' + str(result3))
        history.insert(0, f'{num1} {a} {num2} = {result3}')

    if a != '+' and a != '-' and a != '*' and a != '/':
        print('\n⚠️!ALER!⚠️try again\nThe problem in +, -, *, or / ...\n')
        calculadora()
    else: pass

    if len(history) >= 6:
        history.pop(5)

    e = input("\nShow history? \nyes/no: ")
    if e == 'yes' or e == 'Yes' or e == 'YES':
        for record in history:
            print(record)
    else:
        pass



    b = input("\nStop? \nyes/no: ")
    if b == 'yes' or b == 'Yes' or b == 'YES':
        shutdown()
    else:
        calculadora()


calculadora()
