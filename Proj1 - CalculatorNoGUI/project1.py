# Print greeting message, list available commands, show syntax
print('''\
------------------------------------------
    Hey, I am a calculator.
------------------------------------------
''')
print('''\
    List of commands:
    -q --> quit
    + --> addition
    - --> subtraction
    * --> multiplication
    / --> classic division
    ** --> exponential 
''')
print('''\
For this calculator to work properly, please type in this format:
<command> <value1> <value2>
''')

run_flag = 1
while run_flag:
    # Wait for user input
    ui = input("--> ")
    
    # Extract arguments into a list
    uiArgs = ui.split(' ')
    command, v1, v2 = uiArgs
    
    if command != '-q':
        # Convert values from strings into their respective types
        if '.' in v1:
            v1 = float(v1)
        else:
            v1 = int(v1)
        if '.' in v2:
            v2 = float(v2)
        else:
            v2 = int(v2)
            
        # Parse command
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
        # Print result
        print(result)
    elif command == '-q':
        run_flag = 0
        print('Exiting Calculator...')