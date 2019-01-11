#https://www.coderbyte.com/editor/First%20Reverse:Python#

#Difficulty - Easy

#Recursion!

def FirstFactorial(num): 
    if num == 1:
        return 1
    else:
        return num * FirstFactorial(num - 1)
print FirstFactorial(raw_input())
