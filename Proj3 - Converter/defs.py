import argparse

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

    ('mm', 'nm'): 1e+6,
    ('mm', 'um'): 1000,
    ('mm', 'mm'): 1,
    ('mm', 'cm'): 0.1,
    ('mm', 'm'): 0.001,
    ('mm', 'km'): 1e-6,
    ('mm', 'in'): 0.0393701,
    ('mm', 'ft'): 0.00328084,
    ('mm', 'yd'): 0.00109361,
    ('mm', 'mi'): 6.2137e-7,

    ('cm', 'nm'): 1e+7,
    ('cm', 'um'): 10000,
    ('cm', 'mm'): 10,
    ('cm', 'cm'): 1,
    ('cm', 'm'): 0.01,
    ('cm', 'km'): 1e-5,
    ('cm', 'in'): 0.393701,
    ('cm', 'ft'): 0.0328084,
    ('cm', 'yd'): 0.0109361,
    ('cm', 'mi'): 6.2137e-6,

    ('m', 'nm'): 1e+9,
    ('m', 'um'): 1e+6,
    ('m', 'mm'): 1000,
    ('m', 'cm'): 100,
    ('m', 'm'): 1,
    ('m', 'km'): 0.001,
    ('m', 'in'): 39.3701,
    ('m', 'ft'): 3.28084,
    ('m', 'yd'): 1.09361,
    ('m', 'mi'): 0.000621371,

    ('km', 'nm'): 1e+12,
    ('km', 'um'): 1e+9,
    ('km', 'mm'): 1e+6,
    ('km', 'cm'): 100000,
    ('km', 'm'): 1000,
    ('km', 'km'): 1,
    ('km', 'in'): 39370.1,
    ('km', 'ft'): 3280.84,
    ('km', 'yd'): 1093.61,
    ('km', 'mi'): 0.621371,

    ('in', 'nm'): 2.54e+7,
    ('in', 'um'): 25400,
    ('in', 'mm'): 25.4,
    ('in', 'cm'): 2.54,
    ('in', 'm'): 0.0254,
    ('in', 'km'): 2.54e-5,
    ('in', 'in'): 1,
    ('in', 'ft'): 0.0833333,
    ('in', 'yd'): 0.0277778,
    ('in', 'mi'): 1.5783e-5,

    ('ft', 'nm'): 3.048e+8,
    ('ft', 'um'): 304800,
    ('ft', 'mm'): 304.8,
    ('ft', 'cm'): 30.48,
    ('ft', 'm'): 0.3048,
    ('ft', 'km'): 0.0003048,
    ('ft', 'in'): 12,
    ('ft', 'ft'): 1,
    ('ft', 'yd'): 0.333333,
    ('ft', 'mi'): 0.000189394,
    
    ('yd', 'nm'): 9.144e+8,
    ('yd', 'um'): 914400,
    ('yd', 'mm'): 914.4,
    ('yd', 'cm'): 91.44,
    ('yd', 'm'): 0.9144,
    ('yd', 'km'): 0.0009144,
    ('yd', 'in'): 36,
    ('yd', 'ft'): 3,
    ('yd', 'yd'): 1,
    ('yd', 'mi'): 0.000568182,
    
    ('mi', 'nm'): 1.60934e+12,
    ('mi', 'um'): 1.60934e+9,
    ('mi', 'mm'): 1.609e+6,
    ('mi', 'cm'): 160934,
    ('mi', 'm'): 1609.34,
    ('mi', 'km'): 1.60934,
    ('mi', 'in'): 63360,
    ('mi', 'ft'): 5280,
    ('mi', 'yd'): 1760,
    ('mi', 'mi'): 1
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

    ('g', 'ug'): 1e+6,
    ('g', 'mg'): 1000,
    ('g', 'g'): 1,
    ('g', 'kg'): 0.001,
    ('g', 'oz'): 0.035274,
    ('g', 'lb'): 0.00220462,
    ('g', 'USton'): 1.1023e-6,

    ('kg', 'ug'): 1e+9,
    ('kg', 'mg'): 1e+6,
    ('kg', 'g'): 1000,
    ('kg', 'kg'): 1,
    ('kg', 'oz'): 35.274,
    ('kg', 'lb'): 2.20462,
    ('kg', 'USton'): 0.00110231,

    ('oz', 'ug'): 2.835e+7,
    ('oz', 'mg'): 28349.5,
    ('oz', 'g'): 28.3495,
    ('oz', 'kg'): 0.0283495,
    ('oz', 'oz'): 1,
    ('oz', 'lb'): 0.0625,
    ('oz', 'USton'): 3.125e-5,

    ('lb', 'ug'): 4.536e+8,
    ('lb', 'mg'): 453592,
    ('lb', 'g'): 453.592,
    ('lb', 'kg'): 0.453592,
    ('lb', 'oz'): 16,
    ('lb', 'lb'): 1,
    ('lb', 'USton'): 0.0005,

    ('USton', 'ug'): 9.072e+11,
    ('USton', 'mg'): 9.072e+8,
    ('USton', 'g'): 907185,
    ('USton', 'kg'): 907.185,
    ('USton', 'oz'): 32000,
    ('USton', 'lb'): 2000,
    ('USton', 'USton'): 1
}
dispDict = {'length': lengthDict, 'mass': massDict}

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
    
def unit_convert(type, num, unit, convertUnit):
    if type in dispDict:
        dictRef = dispDict[type]
        if (unit, convertUnit) in dictRef:
            convRatio = dictRef[(unit, convertUnit)]
            return num * convRatio
        else:
            return 'Error: invalid unit conversion. Units are either undefined or spelled incorrectly.'
    else:
        return 'Error: invalid discipline. Name of discipline is either undefined or spelled incorrectly.'
    pass