'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

def accum(string):
    string = list(string)
    new_string = []
    count = 1
    for i in string:
        new_string.append(i*count)
        count += 1
    for k,v in enumerate(new_string):
        new_string[k] = v.title()
    return '-'.join(new_string)