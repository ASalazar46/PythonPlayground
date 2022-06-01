import defs

clArgs = defs.get_arguments()
#print('Arguments received: ', clArgs)

result = defs.unit_convert(
    clArgs.type, 
    clArgs.number, 
    clArgs.unit, 
    clArgs.convertUnit
)
print(result, clArgs.convertUnit)