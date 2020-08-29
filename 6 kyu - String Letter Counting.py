'''
Take an input string and return a string that is made up of the number of occurences of each english letter in the 
input followed by that letter, sorted alphabetically. The output string shouldn't contain chars missing from input 
(chars with 0 occurence); leave them out.

An empty string, or one with no letters, should return an empty string.

Notes:
    * the input will always be valid;
    * treat letters as case-insensitive

Examples
"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  ""
'''

alfabeth = list('abcdefghijklmnopqrstuvwxyz')
def string_letter_count(string):
    string = list(string.lower()); string = [i for i in string if i in alfabeth]; string2 = string.copy(); string2 = sorted(list(set(string2))); count = []; array = []
    for i in string2:
        count.append(string.count(i))
    for a,b in zip(string2, count):
        array.append(str('{}{}'.format(b,a)))
    return ''.join(array)