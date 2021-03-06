import argparse
import secrets
import string

# Handle the generation of the password given the arguments from
# the command line
def GenPass(length, setFlags):
    if length <= 0:
        return 'Error: Password length cannot be 0 or less. Try again.'
    symbolSet = ''
    for flag in setFlags:
        match flag:
            case 'l':
                symbolSet += string.ascii_lowercase
            case 'u':
                symbolSet += string.ascii_uppercase
            case 'p':
                symbolSet += string.punctuation
            case 'n':
                symbolSet += string.digits
            case _:
                return 'Error: cannot parse argument `symbols`.\nTry again, or type \'py project2.py -h\' for help.'
    return ''.join(secrets.choice(symbolSet) for char in range(length))

# Process arguments from command line
# First step: create a parser
parserObj  = argparse.ArgumentParser(description='Generate a password.')

# Second step: fill in argument information
# One for `passLength` ...
parserObj.add_argument('passLength', type=int, help='Desired password length. Length must be greater than 0.')

# Another for `symbols` ...
h1 = 'Inclusion of symbol sets within password.'
h2 = "'l' --> lower case letters"
h3 = "'u' --> upper case letters"
h4 = "'p' --> punctuation marks"
h5 = "'n' --> numbers"
helpMsg = h1+h2+h3+h4+h5
parserObj.add_argument('symbols', help=helpMsg)

# Finally, acquire the arguments from the command line
clArgs = parserObj.parse_args()
#print(clArgs.passLength, clArgs.symbols)

# Generate the password using the arguments
print(GenPass(clArgs.passLength, clArgs.symbols))

