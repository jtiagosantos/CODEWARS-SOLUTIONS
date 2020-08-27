'''
For this Kata you will have to forget how to add two numbers together.

The best explanation on what to do for this kata is this meme :

https://i.ibb.co/Y01rMJR/caf.png

In simple terms our method does not like the principle of carrying over numbers and just writes down every number it calculates.

You may assume both integers arepositive integersand the result will not be bigger than Integer.MAX_VALUE (only for java)
'''

def add(num1, num2):
    num1 = [int(i) for i in list(str(num1))]
    num2 = [int(i) for i in list(str(num2))]
    soma = []
    if len(num1) != len(num2):
        dif = abs(len(num1) - len(num2))
        if len(num1) > len(num2):
            for _ in range(dif):
                num2.insert(0, 0)
        elif len(num2) > len(num1):
            for _ in range(dif):
                num1.insert(0, 0)

    for a,b in zip(num1[::-1], num2[::-1]):
        soma.append(a+b)

    return int(''.join([str(i) for i in soma[::-1]]))

