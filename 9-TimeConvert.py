

# https://www.coderbyte.com/editor/Time%20Convert:Python#
# Difficulty easy
# Implemented floor division //

def TimeConvert(num): 

    # code goes here 
    
    # input is num and the output is a format hours:mins, be mindfuls of str and int concatenation (close call!)
    
    hours = num//60
    mins = num%60
    
    return str(hours) + ':' + str(mins)
    
# keep this function call here  
print TimeConvert(raw_input())