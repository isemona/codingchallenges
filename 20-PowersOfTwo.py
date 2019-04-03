# https://www.coderbyte.com/editor/Powers%20of%20Two:Python#
# Difficulty Easy
# Implemented a while loop


def PowersofTwo(num): 
    while num % 2 == 0:
        num = num / 2
    if num == 1:
        return 'true'
    return 'false'
    
print PowersofTwo(raw_input())


