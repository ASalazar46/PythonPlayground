# Title: Converter
## Project Number: 3
## Team: Andrew Salazar 
### Overview: 
Command line application that contains multiple converters. 
### Context:
Modern calculators usually have built in converters. While this will not
be an extension to the calculator in [project 1](../Proj1%20-%20CalculatorNoGUI/),
I would still like to implement converters of all sorts in this project. 
### Goals:
- Complete the project according to the proposed solution.
- Experience more Python application building.
- Write more design documents.
### Achieved Milestones:
- [5/28/2022] Project files created
### Proposed Solution:
Similar to [project 2](../Proj2%20-%20PasswordGenerator), the script will run from the command line. It will take three arguments: a number, the unit for that number, and the unit to convert to. Running the script in the command line as `py project3.py <number> <unit> <convertTo>` should calculate and print the value of the converted unit. 

Reading arguments from the command line will be done with the `argparse` module. Create an `ArgumentParser` object that defines arguments with `add_argument()` and parses arguments with `parse_arguments()`. From there the arguments are passed to a function that will calculate and return the value of the converted unit. Let's call this function `unit_convert()`.


### Current Progress/Solution:
asdf