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
For me to work properly, please type your input in this format:
<command> <value1> <value2>
''')

run_flag = 1
while run_flag:
    # Wait for user input
    x = input("--> ")
    print('Your input is: ', x)
# Check for correct syntax input

# Check for undefined command input