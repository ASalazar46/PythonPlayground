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
-[5/24/2022] README file created, project started.
-[5/26/2022] README file filled in, up to proposed solution
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
asdf