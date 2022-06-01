import defs

clArgs = defs.get_arguments()

print(defs.unit_convert(
    clArgs.type, 
    clArgs.number, 
    clArgs.unit, 
    clArgs.convertUnit
), clArgs.convertUnit)
