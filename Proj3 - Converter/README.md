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

asdf
