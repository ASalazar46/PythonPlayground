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
-[5/24/2022] README file created and filled in, up to the proposed solution.
### Proposed Solution:
Normally, in the process of making a user account, websites have their own rules that a user's password must adhere to. This application should be able to generate a password that follow these rules. Two common rules include the use of alphanumeric symbols (including punctuation marks), and password lengths within a specified minimum - maximum range. More rules possibly exist, but these two are the most common, and will serve as the base of a complete application.

A user should be able to specify these rules as keyword arguments to pass to the script, rather than running the script and inputting rules from code-prompted inputs like `input()`. (i.e: I want to pass arguments to the command terminal like: `py myscript.py <command> <kwArgs>`). 

For the length requirement, `minLength` and `maxLength` determine the password length range, and both of these arguments take integers. Of course, `minLength` should be greater than 0, and `maxLength` should be a reasonable integer value. If the value of `maxLength` is less than the value of `minLength`, then display an error that says something like "Max length is smaller than min length. Try again." Providing the same value for `minLength` and `maxLength` will generate the password of that length. 

For alphanumeric symbols: `symbols` takes a string that signal the application to include certain symbols sets in password generation. 
- 'l' to include lower case letters
- 'u' to include upper case letters
- 'p' to include punctuation marks
- 'n' to include numbers 
For example, if I wanted only numbers and punctuaton marks within my password, then for the `symbols` argument I would type 'np' or 'pn' as the value (remove the single quotes when typing it in the terminal, and order of the letters should not matter).

Perhaps a '-h' command could displays a help screen containing all the information needed to use this application. A '-g' command signals the application to generate a password given the specified keyword arguments.

The standard Python library contains a subset of modules that specialize in cryptographic services. Apart of these modules is the `secrets` module. This module will prove to be useful in making the generation of passwords as random as possible. 

There is the `random` module that generates pseudo-random numbers. This was my first option to use for random generation, until I read the documentation and changed my mind. It states that the `random` module is better suited for probability and statistics, and not cryptography.
### Current Progress/Solution:
asdf