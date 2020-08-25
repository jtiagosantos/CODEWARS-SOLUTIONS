'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9² is 81 and 1² is 1.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    num = list(str(num))
    for k,v in enumerate(num):
        num[k] = int(v)
    num = [i ** 2 for i in num]
    return int(''.join([str(i) for i in num]))