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
- [5/22/2022 @ 11:26 PM] Finished README. Project, as by the proposed solution, is declared COMPLETE. 

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
# defs.py
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
Three print statements: one for the greeting message, one for the list of commands, and one for the proper syntax. ~~Don't need to make it any more complex than that.~~ Moved these print statements to a new file called `defs.py`. This decision was meant to shorten the length of `project1.py` and make it more readable, as with the other functions moved to `defs.py`.

```python
# project1.py
# Print greeting message, list available commands, show syntax
defs.startupMessage()
```

> The script should then wait for user input that follows the syntax. Perhaps store user inputs in a list. The list should be of length 3 to execute commands or of length 1 only if quitting the script, else display an error for not following syntax. 

This part was implemented as follows:

```python
# project1.py
# Get input
ui = input("--> ")

# Process inputs
noWSArgs = defs.processInput(ui)
    ...
```
```python
# defs.py
def processInput(x):
    argList = x.split(' ')

    modfiedList = []
    for arg in argList:
        if arg != ' ' and arg != '':
            modfiedList.append(arg)

    return modfiedList 
```
User inputs were received and passed to `processInput(x)` for processing. The definition of this is written in the `defs.py` file. The input is split into a list called `argList` via the string method `split(' ')`, and sanitized to remove list arguments that were whitespaces or empty. A `for` loop handled this well and held the modified list contents in a new list called `modfiedList`. `modfiedList` is returned and stored in the `noWSArgs` variable.

```python
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
```

Enforcement of the syntax involved checking for specific cases. If `len(noWSArgs) > 3`, then there are too many arguments. If `len(noWSArgs) < 3 and noWSArgs[0] == '-q'`, then raise the flag to quit the application. If the quit command is absent, but `len(noWSArgs) < 3`, then there are not enough arguments. If `len(noWSArgs) == 3`, then the script proceeds with the next part of the code.

> If the operator is invalid or undefined, display an error and continue waiting for input. Internally, functions will handle singular mathematical operation and prevent unhandled errors. If the values passed to the functions are invalid for the operator (e.g: giving strings instead of ints to an addition operator), display an error and wait for more user input. Specifically, for division-type ops, display an error if value2 is zero (no dividing by zero). Print the result upon success, and continue to wait for more user input. Quitting the script should be its own command, possibly something like '-Quit.'

The implementation of this part of the spec is as follows:

```python
# project1.py
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
```
```python
# defs.py
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

...

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

...

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
```

`executeCommand(command, v1, v2)`, defined in `defs.py`, holds a `match` code block that determines valid commands (operators). If defined in the `match` block as its own case, then it is a valid command. There is a default case that is a catch-all for undefined commands. In this default case an error message is returned, to be printed. 

~~However, commands currently are not written as functions, but operate just fine.~~ Command definitions have been functionized in `defs.py`, as per the proposed solution. Values `v1` and `v2` are converted from a string to their respective numeric types via `str2Val(x)`. If either were unable to convert to a numeric data type, it was considered NaNN (Not a Numeric Number), which prints an error. The division command now handles the divide-by-zero error by returning an error message, rather than a numeric value.