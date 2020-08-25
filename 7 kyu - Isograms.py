'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Examples
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''

def is_isogram(string):
    count = 0
    string = string.lower()
    string = list(string)
    for i in string:
        if string.count(i) > 1:
            count += 1
    if count > 0 :
        return False
    elif count == 0 or string == []:
        return True