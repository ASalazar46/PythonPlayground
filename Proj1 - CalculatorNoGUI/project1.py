# Print greeting message, list available commands, show syntax
from multiprocessing.sharedctypes import Value

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

# Keep processing input until quitting time
run_flag = True
while run_flag:
    # Get input
    ui = input("--> ")
    # Place inputs into a list
    uiArgs = ui.split(' ')
    
    # Remove excess whitespaces and empty chars, '', from args list
    noWSArgs = []
    for arg in uiArgs:
        if arg != ' ' and arg != '':
            noWSArgs.append(arg)
    
    # Check for syntax errors and undefined commands
    # If no errors, proceed with calculations.
    if len(noWSArgs) < 3:
        if len(noWSArgs) == 1 and noWSArgs[0] == '-q':
            run_flag = False
        else:    
            print('Not enough arguments. Try again.')
    elif len(noWSArgs) > 3:
        print('Too many arguments. Try again.')
    elif len(noWSArgs) == 3:
        command, v1, v2 = noWSArgs
        print(command, v1, v2)

        if '.' in v1:
            try:
                v1 = float(v1)
            except ValueError:
                v1 = 'NaNN'
        else:
            try:
                v1 = int(v1)
            except ValueError:
                v1 = 'NaNN'
        if '.' in v2:
            try:
                v2 = float(v2)
            except ValueError:
                v2 = 'NaNN'
        else:
            try:
                v2 = int(v2)
            except ValueError:
                v2 = 'NaNN'

        if v1 == 'NaNN' or v2 == 'NaNN':
            print('Numeric values only. Try again.')
        else: 
            result = 0
            match command:
                case '+':
                    result = v1 + v2
                case '-':
                    result = v1 - v2
                case '*':
                    result = v1 * v2
                case '/':
                    if v2 == 0:
                        print('No dividing by 0. Try again.')
                    else:
                        result = v1 / v2
                case '**':
                    result = v1 ** v2
                case _:
                    result = "Unknown command. Try again."

            print(result)
print('Exiting Calculator.')