# https://www.coderbyte.com/editor/Simple%20Symbols:Python
# Difficulty Easy
# Implemented nested if statments and if not condition

def SimpleSymbols(s): 
    s = '=' + s + '='
    for i in s:
        if i in 'qwertyuiopasdfghjklzxcvbnm':
            if not s[s.index(i) - 1] == '+' or not s[s.index(i) + 1] == '+':
                return 'false'
    return 'true'
print SimpleSymbols(raw_input())