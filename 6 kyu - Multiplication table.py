'''
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9

for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
'''

def multiplication_table(size):
    table = []
    i = 1
    m = 1
    for _ in range(size):
        sub_table = []
        m = 1
        for _ in range(size):
            sub_table.append(i*m)
            m += 1
        i += 1
        table.append(sub_table)
        
    return table