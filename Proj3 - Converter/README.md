# Title: Unit Converter

## Project Number: 3

## Team: Andrew Salazar

### Overview

Command line application that contains multiple converters.

### Context

Modern calculators usually have built in converters. While this will not
be an extension to the calculator in [project 1](../Proj1%20-%20CalculatorNoGUI/), I would still like to implement converters of all sorts in this project.

### Goals

- Complete the project according to the proposed solution.
- Experience more Python application building.
- Write more design documents.

### Achieved Milestones

- [5/28/2022] Project files created
- [5/30/2022] Completed README, up to proposed solution
- [6/1/2022] Completed README. Minimum spec achieved.

### Proposed Solution

This application should be able to convert one unit to another unit of the same discipline (e.g: millimeters can be converted into meters because they are of the same discipline, length). The minimum spec of this project is:

- Implement the 'mass' and 'length' discipline types
- Implement common sub-units of each discipline
  - Length:
    - Metric: nano-, micro-, milli-, centi-, base, kilo-
    - Imperial: inch, foot, yard, mile
  - Mass:
    - Metric: micro-, milli-, base, kilo-
    - Imperial: ounce, pound, US ton
- Calculate and display the correct conversion

Running the script from the command line should look like: `py project3.py <type> <number> <unit> <convertUnit>`. `type` specifies which discipline of measurement to focus on. `number` is the value to convert. `unit` is the unit of `number`. `convertUnit` is the unit to convert `number` to. `number` should take either an integer or a float. `type`, `unit`, and `convertUnit` should accept strings.

Reading arguments from the command line will be done with the `argparse` module. Create an `ArgumentParser` object that defines arguments with `add_argument()` and parses arguments with `parse_arguments()`. The arguments are passed to a function that will calculate and return the value of the converted unit. The result should be `print()`ed out to the command line. Let's call the function that calculates the result, `unit_convert(type, number, unit, convertUnit)`.

For example, if I wanted to convert 10 meters into millimeters, then the result would be calculated as such: `10 (m) * 1,000 (mm / m) = 10,000 (mm)`. In this example, the `type` is implied to be 'length', since we are working with units of length. However, we will need to specify `type` to the script so it knows which discipline to work with. `unit` and `convertUnit` are meters and millimeters, respectively. `number` is 10. The distinct pair of `unit` and `convertUnit` will have an associated conversion ratio, which will be used to calculate the result. In this case, the conversion ratio is 1000 (mm) / 1 (m), or 1000 (mm / m). The value of `number` is multiplied by the appropriate conversion ratio, `10 (m) * 1,000 (mm / m) = 10,000 (mm)`, and the product is returned to the function caller to be `print()`ed.

One problem is finding a way to calculate the correct conversion ratio based on the arguments given by `unit` and `convertUnit`. One possible solution is to not calculate it at all and reference hard-coded conversion ratios inside of dictionaries. To start, we have a dictionary containing `type`: dictionary entries. Let's call this dictionary, `dispDict`. `type` is the name of the discipline and 'dictionary' is the discipline's respective dictionary of conversion ratios. Let's call this sub-directory, `<type>Dict`. In this sub-dictionary the entries are of the format, tuple: ratio. 'Tuple' contains the values received from `unit` and `convertUnit`, formatted as (`unit`, `convertUnit`). 'Ratio' is the conversion unit associated with those two units.

Accessing the correct conversion unit will require two dictionary calls, one call to `dispDict` and another to `<type>Dict`. Doing so is written as: `dispDict[type]` and `<type>Dict[(unit, convertUnit)]`, respectively. If `type` is not found within `dispDict`, or `type in dispDict == False`, return an error message. It should say something like, 'Error: invalid discipline. Name of discipline is either undefined or spelled incorrectly.' If (`unit`, `convertUnit`) is not found within `<type>Dict`, or `(unit, convertUnit) in <type>Dict == False`, return an error message. It should say something like, 'Error: invalid unit conversion. Units are either undefined or spelled incorrectly.'

### Current Progress/Solution

>Running the script from the command line should look like: `py project3.py <type> <number> <unit> <convertUnit>`. `type` specifies which discipline of measurement to focus on. `number` is the value to convert. `unit` is the unit of `number`. `convertUnit` is the unit to convert `number` to. `number` should take either an integer or a float. `type`, `unit`, and `convertUnit` should accept strings.

Much like in [project 2](../Proj2%20-%20PasswordGenerator/), arguments were defined and values were retrieved from the command line with the `argparse` module. However, I moved this whole process into its own function called `get_arguments()`, and written in a file caled `defs.py`. This was done for the purpose of very simple `project3.py` readability. It was probably unnecessary to do this, but I felt like doing it. Rather than take up a few lines of code, why not just take up only one? 

```python
# project3.py
import defs

clArgs = defs.get_arguments()
...
```
```python
# defs.py
import argparse

def get_arguments():
    parseArgs = argparse.ArgumentParser(
        description='Convert one unit to another unit.')

    parseArgs.add_argument('type', 
        help='Name of the discipline of measurement.')
    parseArgs.add_argument('number', type=int, 
        help='The value to convert.')
    parseArgs.add_argument('unit', 
        help='The unit of number')
    parseArgs.add_argument('convertUnit',
        help='The unit to convert number to.')

    return parseArgs.parse_args()
```

>Let's call the function that calculates the result, `unit_convert(type, number, unit, convertUnit)`.

There are only three commands in `project3.py`: one to import function definitions from `defs.py`, one to execute the `get_arguments()` function, and one to display the result of the conversion attempt. This function's name is `unit_convert(type, number, unit, convertUnit)`, and is the last command in the `project3.py` file. 

```python
# project3.py
...
print(defs.unit_convert(
    clArgs.type, 
    clArgs.number, 
    clArgs.unit, 
    clArgs.convertUnit
), clArgs.convertUnit)
```
>One problem is finding a way to calculate the correct conversion ratio based on the arguments given by `unit` and `convertUnit`. One possible solution is to not calculate it at all and reference hard-coded conversion ratios inside of dictionaries. To start, we have a dictionary containing `type`: dictionary entries. Let's call this dictionary, `dispDict`. `type` is the name of the discipline and 'dictionary' is the discipline's respective dictionary of conversion ratios. Let's call this sub-directory, `<type>Dict`. In this sub-dictionary the entries are of the format, tuple: ratio. 'Tuple' contains the values received from `unit` and `convertUnit`, formatted as (`unit`, `convertUnit`). 'Ratio' is the conversion ratio associated with those two units.

This was implemented. There are three dictionaries, two for the 'length' and 'mass' sub-units and one for the disciplines themselves. To de-clutter and shorten the length of `defs.py`, these three dictionaries were moved to their own file called `dict.py`. Hard-coding the conversion ratios was not hard, but so very tedious. Maybe an improvement would be finding a way to dynamically calculate each conversion ratio.

```python
# dict.py
lengthDict = {
    ('nm', 'nm'): 1,
    ('nm', 'um'): 0.001,
    ('nm', 'mm'): 1e-6,
    ('nm', 'cm'): 1e-7,
    ('nm', 'm'): 1e-9,
    ('nm', 'km'): 1e-12,  
    ('nm', 'in'): 3.937e-8,
    ('nm', 'ft'): 3.2808e-9,
    ('nm', 'yd'): 1.0936e-9,
    ('nm', 'mi'): 6.2137e-13,

    ('um', 'nm'): 1000,
    ('um', 'um'): 1,
    ('um', 'mm'): 0.001,
    ('um', 'cm'): 1e-4,
    ('um', 'm'): 1e-6,
    ('um', 'km'): 1e-9,
    ('um', 'in'): 3.937e-5,
    ('um', 'ft'): 3.2808e-6,
    ('um', 'yd'): 1.0936e-6,
    ('um', 'mi'): 6.2137e-10,
    ...
}

massDict = {
    ('ug', 'ug'): 1,
    ('ug', 'mg'): 0.001,
    ('ug', 'g'): 1e-6,
    ('ug', 'kg'): 1e-9,
    ('ug', 'oz'): 3.5274e-8,
    ('ug', 'lb'): 2.2046e-9,
    ('ug', 'USton'): 1.1023e-12,

    ('mg', 'ug'): 1000,
    ('mg', 'mg'): 1,
    ('mg', 'g'): 0.001,
    ('mg', 'kg'): 1e-6,
    ('mg', 'oz'): 3.5274e-5,
    ('mg', 'lb'): 2.2046e-6,
    ('mg', 'USton'): 1.1023e-9,
    ...
}

dispDict = {'length': lengthDict, 'mass': massDict}
```
>Accessing the correct conversion unit will require two dictionary calls, one call to `dispDict` and another to `<type>Dict`. Doing so is written as: `dispDict[type]` and `<type>Dict[(unit, convertUnit)]`, respectively. If `type` is not found within `dispDict`, or `type in dispDict == False`, return an error message. It should say something like, 'Error: invalid discipline. Name of discipline is either undefined or spelled incorrectly.' If (`unit`, `convertUnit`) is not found within `<type>Dict`, or `(unit, convertUnit) in <type>Dict == False`, return an error message. It should say something like, 'Error: invalid unit conversion. Units are either undefined or spelled incorrectly.'

After defining the dictionaries required, the last thing to do was program the `unit_convert()` function. As described in the spec, if `type` is a valid discipline in `dispDict`, then access its respective dictionary. If not, then return an error message saying something went wrong. If (`unit`, `convertUnit`) is a valid conversion pair, then return the product of `num` and the appropriate conversion ratio. If not, then return an error message saying something went wrong. `getcontext().prec = 7` and `Decimal(num) * Decimal(convRatio)` are only there to limit the result to 7 significant figures, for readability.

```python
# defs.py
...
import dict
from decimal import *
...
def unit_convert(type, num, unit, convertUnit):
    if type in dict.dispDict:
        dictRef = dict.dispDict[type]
        if (unit, convertUnit) in dictRef:
            convRatio = dictRef[(unit, convertUnit)]
            getcontext().prec = 7
            return Decimal(num) * Decimal(convRatio)
        else:
            return 'Error: invalid unit conversion. Units are either undefined or spelled incorrectly.'
    else:
        return 'Error: invalid discipline. Name of discipline is either undefined or spelled incorrectly.'
```

