import argparse

lengthDict = {
    ('nm', 'nm'): 1,
    ('nm', 'um'): 0.001,
    ('nm', 'mm'): 0.000001,
    ('nm', 'cm'): 0.0000001,
    ('nm', 'm'): 0.000000001,
    ('nm', 'km'): 0.000000000001,  
    ('nm', 'in'): 0.000000039370079,
    ('nm', 'ft'): 0.00000000328084,
    ('nm', 'yd'): 0.000000001093613,
    ('nm', 'mi'): 0.000000000000621,

    ('um', 'nm'): 1000,
    ('um', 'um'): 1,
    ('um', 'mm'): 0.001,
    ('um', 'cm'): 0.0001,
    ('um', 'm'): 0.000001,
    ('um', 'km'): 0.000000001,
    ('um', 'in'): 0.000039,
    ('um', 'ft'): 0.000003,
    ('um', 'yd'): 0.000001,
    ('um', 'mi'): 0.000000000621371,

    ('mm', 'nm'): 1000000,
    ('mm', 'um'): 1000,
    ('mm', 'mm'): 1,
    ('mm', 'cm'): 0.1,
    ('mm', 'm'): 0.001,
    ('mm', 'km'): 0.000001,
    ('mm', 'in'): 0.03937,
    ('mm', 'ft'): 0.003281,
    ('mm', 'yd'): 0.001094,
    ('mm', 'mi'): 0.000000621371192,

    ('cm', 'nm'): 10000000,
    ('cm', 'um'): 10000,
    ('cm', 'mm'): 10,
    ('cm', 'cm'): 1,
    ('cm', 'm'): 0.01,
    ('cm', 'km'): 0.00001,
    ('cm', 'in'): 0.393701,
    ('cm', 'ft'): 0.032808,
    ('cm', 'yd'): 0.010936,
    ('cm', 'mi'): 0.000006,

    ('m', 'nm'): 1000000000,
    ('m', 'um'): 1000000,
    ('m', 'mm'): 1000,
    ('m', 'cm'): 100,
    ('m', 'm'): 1,
    ('m', 'km'): 0.001,
    ('m', 'in'): 39.37008,
    ('m', 'ft'): 3.28084,
    ('m', 'yd'): 1.093613,
    ('m', 'mi'): 0.000621,

    ('km', 'nm'): 1000000000000,
    ('km', 'um'): 1000000000,
    ('km', 'mm'): 1000000,
    ('km', 'cm'): 100000,
    ('km', 'm'): 1000,
    ('km', 'nm'): 1,
    ('km', 'in'): 39370.08,
    ('km', 'ft'): 3280.84,
    ('km', 'yd'): 1093.613,
    ('km', 'mi'): 0.621371,

    ('in', 'nm'): 25400000,
    ('in', 'um'): 25400,
    ('in', 'mm'): 25.4,
    ('in', 'cm'): 2.54,
    ('in', 'm'): 0.0254,
    ('in', 'km'): 0.000025,
    ('in', 'in'): 1,
    ('in', 'ft'): 0.083333,
    ('in', 'yd'): 0.027778,
    ('in', 'mi'): 0.000016,

    ('ft', 'nm'): 304800000,
    ('ft', 'um'): 304800,
    ('ft', 'mm'): 304.8,
    ('ft', 'cm'): 30.48,
    ('ft', 'm'): 0.3048,
    ('ft', 'km'): 0.000305,
    ('ft', 'in'): 12,
    ('ft', 'ft'): 1,
    ('ft', 'yd'): 0.333333,
    ('ft', 'mi'): 0.000189,
    
    ('yd', 'nm'): 914400000,
    ('yd', 'um'): 914400,
    ('yd', 'mm'): 914.4,
    ('yd', 'cm'): 91.44,
    ('yd', 'm'): 0.9144,
    ('yd', 'km'): 0.000914,
    ('yd', 'in'): 36,
    ('yd', 'ft'): 3,
    ('yd', 'yd'): 1,
    ('yd', 'mi'): 0.000568,
    
    ('mi', 'nm'): 1609344000000,
    ('mi', 'um'): 1609344000,
    ('mi', 'mm'): 1609344,
    ('mi', 'cm'): 160934.4,
    ('mi', 'm'): 1609.344,
    ('mi', 'km'): 1.609344,
    ('mi', 'in'): 63360,
    ('mi', 'ft'): 5280,
    ('mi', 'yd'): 1760,
    ('mi', 'mi'): 1
}
massDict = {}
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