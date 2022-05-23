def startupMessage():
    print('''\
    ------------------------------------------
        Hey, I am a calculator.
    ------------------------------------------
    ''')
    print('''\
        List of commands:
        + --> addition
        - --> subtraction
        * --> multiplication
        / --> classic division
        ** --> exponential 
    ''')
    print('''\
    For this calculator to work properly, please type in this format:
    <command> <value1> <value2>

    To quit, just type -q
    ''')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'No dividing by 0. Try again.'
    else:
        return x / y
def exponential(x, y):
    return x ** y

def str2Val(x):
    y = 0
    if '.' in x:
        try:
            y = float(x)
        except ValueError:
            y = 'NaNN'
    else:
        try:
            y = int(x)
        except ValueError:
            y = 'NaNN'
    return y

def processInput(x):
    argList = x.split(' ')

    modfiedList = []
    for arg in argList:
        if arg != ' ' and arg != '':
            modfiedList.append(arg)

    return modfiedList        
    
def executeCommand(com, x, y):
    match com:
        case '-q':
            return 'To quit, just type -q. No need for arguments.'
        case '+':
            return add(x, y)
        case '-':
            return subtract(x, y)
        case '*':
            return multiply(x, y)
        case '/':
            return divide(x, y)
        case '**':
            return exponential(x, y)
        case _:
            return "Unknown command. Try again."