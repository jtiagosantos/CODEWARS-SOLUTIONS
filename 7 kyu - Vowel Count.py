'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

vogais = 'aeiou'

def get_count(input_str):
    count = 0
    input_str = list(input_str)
    for i in input_str:
        if i in vogais:
            count += 1
            
    return count