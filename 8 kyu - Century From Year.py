'''
Introduction
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Task:
Given a year, return the century it is in.

Input, Output Examples:
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
'''

def century(year):
    year = list(str(year))
    for k, v in enumerate(year):
        year[k] = str(v)
    if len(year) <= 2 or ''.join(year) == '100':
        return 1
    elif len(year) == 3:
        if year[-2:] == ['0','0']:
            return int(year[0])
        else:
            return int(year[0]) + 1
    else:
        final = str('{}{}'.format(year[-1], year[-2]))
        del year[-1]
        del year[-1]
        if final == '00':
            return int(''.join(year))
        else:
            return int(''.join(year)) + 1