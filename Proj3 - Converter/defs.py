import argparse
import dict
from decimal import *

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
