# https://www.coderbyte.com/editor/Two%20Sum:Python
# Difficulty Easy 
# Implemented itertools but also a hash table works beautifully here too

import itertools
def TwoSum(a):
    x, sums = a[0], ''
    for pair in list(itertools.combinations(a[1:], 2)):
        if pair[0] + pair[1] == x:
            sums += str(pair[0]) + ',' + str(pair[1]) + ' '
    if sums == '':
        return -1
    return sums
print TwoSum(raw_input())


