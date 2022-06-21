def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0 :
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

print('Is 2020 a leap year?', isLeapYear(2020))

print('Is 2021 a leap year?', isLeapYear(2021))

print('Is 1600 a leap year?', isLeapYear(1600))

print('Is 1700 a leap year?', isLeapYear(1700))

print('Is 1984 a leap year?', isLeapYear(1984))

print('Is 15 a leap year?', isLeapYear(15))

