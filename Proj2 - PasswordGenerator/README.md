# Title: Password Generator
## Project Number: 2
## Team: Andrew Salazar 
### Overview: 
A command line application that generates a password.
### Context:
It is one thing to be able to remember a password, but another thing to come up with a password in the first place. I chose to work on this project for sake of being able to generate passwords for myself without having to put a lot of effort into making one. 
### Goals:
- Complete the project according to the proposed solution.
- Experience more Python application building.
- Write more design documents.
### Achieved Milestones:
- [5/24/2022] README file created, project started.
- [5/26/2022] README file filled in, up to proposed solution
- [5/27/2022] README filled in, up to current solution. Project (minimum specs) declared COMPLETE
### Proposed Solution:
Normally, in the process of making a user account, websites have their own rules that a user's password must adhere to. This application should be able to generate a password that follow these rules. Two common rules include the use of alphanumeric symbols (including punctuation marks), and password length requirements. More rules possibly exist, but these two rules are the most common, and will serve as the base of a complete application.

In order for this application to work, the script must be able to acquire and parse arguments. The script could just use `input()` and directly prompt the user for input. However, this time around, the arguments must be passed directly to the command line. To solve this issue the script will use the `argparse` module. In this module are methods that will handle the heavy lifting of argument parsing. All I need to do is create an `ArgumentParser` object, define argument information via the `add_argument()` method, and use the `parse_args()` method to retrieve arguments from the command line. The syntax of the command should look something like this: `py project2.py <passLength> <symbols>`.

The first positional argument, `passLength`, determines the password length, and takes an integer. Of course, the value of `passLength` should be greater than 0 and should be a reasonable value. For example, if a website requires a password length between 8 and 16 characters long, then a reasonable value for `passLength` is a value between 8 and 16 characters, including 8 and 16. If `passLength` is less than or equal to zero, then display an error that says something like "Password length cannot be zero or negative. Try again." 

For alphanumeric symbols: `symbols`, the second positional argument, takes a string that signals the application to include certain symbols sets in password generation.
- 'l' to include lower case letters
- 'u' to include upper case letters
- 'p' to include punctuation marks
- 'n' to include numbers 
For example, if I wanted only numbers and punctuaton marks within my password, then for the `symbols` argument I would type 'np' or 'pn' as the value (remove the single quotes when typing it in the terminal, and order of the letters should not matter).

The standard Python library contains a subset of modules that specialize in cryptographic services. Apart of these modules is the `secrets` module. This module will prove to be useful in making the password generation process as random as possible. The `secrets.choice()` method will be utilized in order to randomly select an item from the sequence defined by `symbols`. This is repeated n amount of times - where n is the integer defined by `passLength`. The chosen symbol for each run of `secrets.choice()` will be concatenated to produce the resulting password. 

### Current Progress/Solution:
> Two common rules include the use of alphanumeric symbols (including punctuation marks), and password length requirements. More rules possibly exist, but these two rules are the most common, and will serve as the base of a complete application.

The base specs have been implemented, but it took way less time than expected I initially expected. While the base spec of project completion has been achieved, I will definitely add more to this project.

> In order for this application to work, the script must be able to acquire and parse arguments. The script could just use `input()` and directly prompt the user for input. However, this time around, the arguments must be passed directly to the command line. 

Done. By making use of the `argparse` module and the methods of argument parsing within, I effectively sacrifice the ability to run the script without passing command line arguments. First off, the script requires an argument parser object. Simply creating an object that points to the `ArgumentParser` class is enough. The `add_argument()` method allowed me to define the two arguments, `passLength` and `symbols`. `parse_args()` handled the job of collecting the arguments from the command line. Typing `py project2.py` in the command line will return an error saying that arguments are missing.

```python
# Process arguments from command line
# First step: create a parser
parserObj  = argparse.ArgumentParser(description='Generate a password.')

# Second step: fill in argument information
# One for `passLength` ...
parserObj.add_argument('passLength', type=int, help='Desired password length')

# Another for `symbols` ...
parserObj.add_argument('symbols', help='Inclusion of symbol sets within password.')

# Finally, acquire the arguments from the command line
clArgs = parserObj.parse_args()
```

> The first positional argument, `passLength`, determines the password length, and takes an integer. Of course, the value of `passLength` should be greater than 0 and should be a reasonable value. For example, if a website requires a password length between 8 and 16 characters long, then a reasonable value for `passLength` is a value between 8 and 16 characters, including 8 and 16. If `passLength` is less than or equal to zero, then display an error that says something like "Password length cannot be zero or negative. Try again."

There is a keyword argument in the `add_argument()` method that allows me to specify what types of values an argument can accept. The argument is called `type=`, and it was given `int` as a value, which enforces that all values passed to `passLength` should be an integer, otherwise the script returns an error. Also, it was rather simple to enforce that `passLength` be greater than 0. All it took was an `if` statement with the condition of `passLength <= 0`, then `return error_msg`. As for `passLength` being a 'reasonable' value, I later realized that 'reasonable' is completely dependent on the user. As such, I did not see any reason to write checks for reasonable `passLength` values, and leave it to the user to make the 'reasonable' choice for `passLength`. This line of code is as follows:

```python
def GenPass(length, setFlags):
    if length <= 0:
        return 'Error: Password length cannot be 0 or less. Try again.'
...
parserObj.add_argument('passLength', type=int, help='Desired password length')
```

> For alphanumeric symbols: `symbols`, the second positional argument, takes a string that signals the application to include certain symbols sets in password generation.
> - 'l' to include lower case letters
> - 'u' to include upper case letters
> - 'p' to include punctuation marks
> - 'n' to include numbers 
> For example, if I wanted only numbers and punctuaton marks within my password, then for the `symbols` argument I would type 'np' or 'pn' as the value (remove the single quotes when typing it in the terminal, and order of the letters should not matter).

Defining the `symbols` argument was similar to defining `passLength`. However, I did not need to give the keyword argument, `type=`, a value; I left it as its default value: simple strings. Access to the required symbol sets were made possible using the `string` module. There was no complex reason as to why each flag for the symbol sets were labeled as such. 'Lower case letters' starts with an 'l', 'upper case letters' starts with a 'u', 'punctuation marks' starts with a 'p', and 'numbers' starts with an 'n'.
If the `setFlags` argument, which takes the command line argument `symbols`, detects any of these flags in the string, then the flag's corresponding symbol set is added to the sequence called `symbolSet`. A `for` loop and a nested `match` statement took care of this problem. An `if` statement handled the case where no valid flags were detected, which returned an error.

```python
def GenPass(length, setFlags):
    ...
    symbolSet = ''
    for flag in setFlags:
        match flag:
            case 'l':
                symbolSet += string.ascii_lowercase
            case 'u':
                symbolSet += string.ascii_uppercase
            case 'p':
                symbolSet += string.punctuation
            case 'n':
                symbolSet += string.digits
            case _:
                return 'Error: cannot parse argument `symbols`.\nTry again, or type \'py project2.py -h\' for help.'
...
parserObj.add_argument('symbols', help='Inclusion of symbol sets within password.')
```
> The standard Python library contains a subset of modules that specialize in cryptographic services. Apart of these modules is the `secrets` module. This module will prove to be useful in making the password generation process as random as possible. The `secrets.choice()` method will be utilized in order to randomly select an item from the sequence defined by `symbols`. This is repeated n amount of times - where n is the integer defined by `passLength`. The chosen symbol for each run of `secrets.choice()` will be concatenated to produce the resulting password. 

This part of the code was easy to implement. In fact, one of the tutorials on the `secrets` module documentation page provides a way to use its methods to generate passwords. From that tutorial, I just needed to use the `secrets.choice()` method to pick a random symbol from the available symbol sets, join the result to an existing string, and repeat those steps until the desired password length has been achieved. Typically, in the context of cryptography, it is best practice to avoid saving the password, or parts of the password, in recoverable formats, such as variables.

```python
def GenPass(length, setFlags):
    ...
    return ''.join(secrets.choice(symbolSet) for char in range(length))
...
print(GenPass(clArgs.passLength, clArgs.symbols))
```