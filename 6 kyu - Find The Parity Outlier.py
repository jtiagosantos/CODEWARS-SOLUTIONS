'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
 Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''

def find_outlier(numbers):
    num_par = num_impar = count_par = count_impar = 0
    for i in numbers:
        if i % 2 == 0:
            num_par = i
            count_par += 1
        else:
            num_impar = i
            count_impar += 1
    
    if count_par == 1:
        return num_par
    if count_impar == 1:
        return num_impar