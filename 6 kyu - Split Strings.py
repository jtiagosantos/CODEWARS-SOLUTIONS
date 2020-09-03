'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd 
number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''

def solution(string):
    array = []
    string = list(string)
    while len(string) > 1:
        array.append(''.join(string[:2]))
        del string[0]
        del string[0]
    if len(string) == 1:
        array.append(str('{}_'.format(string[0])))
    return array
    return []