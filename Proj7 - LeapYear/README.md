# Leap Year Checker

## Project Number: 7

## Team: Andrew Salazar

### Overview

Check if a year is a leap year. Return true if the year is a leap year,
otherwise return false.

### Context

There are years when there are 366 days instead of 365 days. More accurately there are approximately 365.25 days in a year, leap or not. Since there is no way to have 1/4 of a day in a year, this leftover amount is accumulated with each passing year. When this amount has accumulated enough to justify the extra full day, the full day is added to the month of February. The year when this happens is considered a leap year.

Everyone knows when a leap year is because of the extra day in February. Take a look at a calendar and take a look at the month of February. If the month ends on the 28th, the year is not a leap year. If on the 29th, then the year is a leap year. But how is this calculated, and how can I accomplish this in a software application?

### Goals

- Experience more Python application building.
- Write more design documents.
- Complete project according to a proposed solution.

### Achieved Milestones

- [6/21/2022] Project files created.

### Proposed Solution

There are specific conditions that make a year a leap year:

- The year is divisible by 4
- The year is NOT divisible by 100
- The year is divisible by 400

Use conditional statements to check for these conditions, and return true or false if conditions are met or not met.

### Current Progress/Solution

```Python
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0 :
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
```

Single-statement conditionals check for each condition.