'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Examples:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ])
# returns 'Bart'
namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''

def namelist(names):
    if len(names) == 1:
        return names[0]['name']
    if names == []:
        return ''
    return '{} & {}'.format(', '.join([i['name'] for i in names[:-1]]), names[-1]['name'])