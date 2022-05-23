import defs

# Print greeting message, list available commands, show syntax
defs.startupMessage()

# Keep processing input until quitting time
run_flag = True
while run_flag:
    # Get input
    ui = input("--> ")
    
    # Process inputs
    noWSArgs = defs.processInput(ui)
    
    # Check for syntax errors and the quit command.
    # If no errors and no quit command, proceed with calculations.
    if len(noWSArgs) < 3:
        if len(noWSArgs) == 1 and noWSArgs[0] == '-q':
            run_flag = False
            print('Quit command received.')
        else:    
            print('Not enough arguments. Try again.')
    elif len(noWSArgs) > 3:
        print('Too many arguments. Try again.')
    elif len(noWSArgs) == 3:
        command, v1, v2 = noWSArgs
        
        # Convert v1, v2 into numeric data types
        v1 = defs.str2Val(v1)
        v2 = defs.str2Val(v2)

        # Check for non numeric values
        # Otherwise, do calculations
        if v1 == 'NaNN' or v2 == 'NaNN':
            print('Numeric values only. Try again.')
        else: 
            result = defs.executeCommand(command, v1, v2)
            print(result)
print('Exiting Calculator.')