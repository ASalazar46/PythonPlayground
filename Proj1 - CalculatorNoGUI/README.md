# Title: Calculator No GUI
## Project Number: 1
## Team: Andrew Salazar (just me)
### Overview: 
A command line application that functions as a calculator. Will
save implementing a GUI for a different project.

### Context:
After reading through the Python tutorial provided by the official 
[doc page](http://docs.python.org/3.10/tutorial), I searched for
beginner Python projects. This idea was one of the first that I saw, 
and I chose to do this project first. 

### Goals:
From this project, I will:
- Learn the basics of organizing Python code into applications (no 
    matter how small or useless they are to anyone). 
- Take my first steps towards becoming accustomed to project building. 
- Become familiar with writing design documents (even if small at first).
- Create an application that functions as a standard, not scientific, 
calculator.
### Achieved Milestones:
- [5/20/2022] Project folder and design document (this README.md) created.
- [5/22/2022] Implemented working EMDAS operations with syntax, value, and operation error checks.

### Proposed Solution:
This calculator should be able to handle EMDAS operations, at minimum, to
be considered complete. EMDAS stands for: exponentials, multiplication, 
division, addition, and subtraction.

Running the script should display these things first:
- A greeting message
- A list of commands
- The syntax required to properly pass arguments to the script which is: {operator} {value1} {value2}

The script should then wait for user input that follows the syntax. Perhaps 
store user inputs in a list. The list should be of length 3 to execute 
commands or of length 1 only if quitting the script, else display an error for not following syntax. 

If the operator is invalid or undefined, display an error and continue waiting for input. Internally, functions will handle singular mathematical operation and prevent unhandled errors. If the values passed to the functions are invalid for the operator (e.g: giving strings instead of ints to an addition operator), display an error and wait for more user input. Specifically, for division-type ops, display an error if value2 is zero (no dividing by zero). Print the result upon success, and continue to wait for more user input. Quitting the script should be its own command, possibly something like '-Quit.'
### Current Progress/Solution:
>This calculator should be able to handle EMDAS operations, at minimum, to
>be considered complete. EMDAS stands for: exponentials, multiplication, 
>division, addition, and subtraction.

These operations were implemented.

> Running the script should display these things first:
> - A greeting message
> - A list of commands
> - The syntax required to properly pass arguments to the script which is: {operator} {value1} {value2}

Wrote this part of the code as follows:
```python
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
```
Three print statements: one for the greeting message, one for the list of commands, and one for the proper syntax. Don't need to make it any more complex than that.

> The script should then wait for user input that follows the syntax. Perhaps store user inputs in a list. The list should be of length 3 to execute commands or of length 1 only if quitting the script, else display an error for not following syntax. 

This part was implemented as follows:
```python
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
    ...
```
User inputs were received, packed into a list called `uiArgs` via the string method `split(' ')`, and sanitized to remove list arguments that were whitespaces or empty. A `for` loop handled this well and held the modified list contents in a new list called `noWSArgs`. 

Enforcement of the syntax involved checking for specific cases. In the case when `len(noWSArgs) > 3`, an error was printed. In the case when the `len(noWSArgs) < 3 and noWSArgs[0] == '-q'`, then set a flag that signals the code to stop receiving inputs. If not this case, but length < 3, then display a syntax error. If `len(noWSArgs) == 3`, then the script proceeded with the next part of the code.

> If the operator is invalid or undefined, display an error and continue waiting for input. Internally, functions will handle singular mathematical operation and prevent unhandled errors. If the values passed to the functions are invalid for the operator (e.g: giving strings instead of ints to an addition operator), display an error and wait for more user input. Specifically, for division-type ops, display an error if value2 is zero (no dividing by zero). Print the result upon success, and continue to wait for more user input. Quitting the script should be its own command, possibly something like '-Quit.'

The current implementation of this part of the spec is as follows:

```python
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
                result = 'No dividing by 0. Try again.'
            else:
                result = v1 / v2
        case '**':
            result = v1 ** v2
        case _:
            result = "Unknown command. Try again."

print(result)
```
The `match` code block controls which commands (operators) are valid. If defined in the `match` block as its own case, then it is a valid command. There is a default case that is a catch-all for undefined commands. In this default case an error is returned, to be printed. 

However, commands currently are not written as functions, but operate just fine. Values `v1` and `v2` are converted from a string to their respective numeric types. If either were unable to convert to a numeric data type, it was considered NaNN (Not a Numeric Number), which prints an error. The division command handles an error when `v2` is zero, which returns an error.