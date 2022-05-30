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
Similar to [project 2](../Proj2%20-%20PasswordGenerator), the script will run from the command line. It will take three arguments: a number, the unit for that number, and the unit to convert to. Running the script in the command line as `py project3.py <number> <unit> <convertUnit>` should calculate and print the value of the converted unit. 

For this project, the appilcation should be able to convert

Reading arguments from the command line will be done with the `argparse` module. Create an `ArgumentParser` object that defines arguments with `add_argument()` and parses arguments with `parse_arguments()`. The arguments are passed to a function that will calculate and return the value of the converted unit. Let's call this function `unit_convert(number, unit, convertUnit)`.

For conversions to work, the script will need the conversion ratio between the unit and the converted unit. For example, if I wanted to convert meters into millimeters then the convertion ratio would be 1000 mm / 1 m, or 1000. If the converting from millimeters to meters then the ratio would be 1 m / 1000 mm, or 1 / 1000. One possible solution is to hard-code all the required convertion ratios and store them in a dictionary for future reference. For each entry in the dictionary, the key would be a tuple containing `(unit, convUnit)`, and the value associated with that key is the convertion ratio between the two. If the tuple of the incoming arguments do not match any of the tuples within the dictionary, return an error. It should say something like, 'Error: Unable to convert value. {unit} to {convUnit} ratio undefined or incorrect spelling of {unit} or {convUnit}. Try again.'

### Current Progress/Solution:
asdf