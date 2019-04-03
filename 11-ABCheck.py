# https://www.coderbyte.com/results/isemona:AB%20Check:Python
# Difficulty Easy
# Used nested if statements

def ABCheck(s): 

    # code goes here 
    # check given string to see if a-b are exactly 3 spaces apart, not counting the spaces
    # if it does return true and if doesn't false
    
    # strip away spaces
    # then loop through the complete string
    # check to see if a
    
    
    
    s = "xx" + s + 'xx' # I thought strings were immutable how are we adding characters here
    for i in range(len(s)):
        if s[i] == "a": # we need the double equals for comparison
            if s[i - 4] == "b" or s[i + 4] == "b": # indexing to find b
                return "true"
    return "false"    
    
    
    
# keep this function call here  
print ABCheck(raw_input())