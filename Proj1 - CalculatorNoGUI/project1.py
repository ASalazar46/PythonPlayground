# Print greeting message, list available commands, show syntax
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
    
    # Check for syntax errors and undefined commands
    # If no errors, proceed with calculations.
    if len(uiArgs) < 3:
        if len(uiArgs) == 1 and uiArgs[0] == '-q':
            run_flag = False
        else:    
            print('Not enough arguments. Try again.')
    elif len(uiArgs) > 3:
        print('Too many arguments. Try again.')
    elif len(uiArgs) == 3:
        command, v1, v2 = uiArgs

        if '.' in v1:
            v1 = float(v1)
        else:
            v1 = int(v1)
        if '.' in v2:
            v2 = float(v2)
        else:
            v2 = int(v2)
            
        result = 0
        match command:
            case '+':
                result = v1 + v2
            case '-':
                result = v1 - v2
            case '*':
                result = v1 * v2
            case '/':
                result = v1 / v2
            case '**':
                result = v1 ** v2
            case _:
                result = "Unknown command. Try again."

        print(result)
print('Exiting Calculator.')