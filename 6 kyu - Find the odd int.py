'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''

def find_it(array):
    for i in array:
        if array.count(i) % 2 != 0:
            return i
