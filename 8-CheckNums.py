# https://www.coderbyte.com/editor/Check%20Nums:Python
# Difficulty easy 
# Implemented math fundamentals


def CheckNums(num1,num2):
    if num2 > num1:
        return 'true'
    elif num2 < num1:
        return 'false'
    return '-1'
print CheckNums(raw_input())