#https://www.coderbyte.com/editor/Swap%20Case:Python
#Difficulty easy
#Implemented built in function .swapcase()

def SwapCase(str): 

    # code goes here
    # swap letters small for cap, i/o str-str mutation; symbols stay as is, refactor
    
    
    new_str = []
    
    for i in str:
        if i == i.lower():
            new_str.append(i.upper())
        else:
            new_str.append(i.lower())
    
    return(''.join(new_str))
        
    
# keep this function call here  
print SwapCase(raw_input())

Using range

def SwapCase(str): 
  
  # in Python there is also a built-in function  
  # that swaps character cases for you 
  # return str.swapcase()

  # turn the string into a list of characters
  chars = list(str)
  
  # loop through the array swapping letter cases
  # uppercase -> lowercase
  # lowercase -> uppercase
  for i in range(0, len(chars)):
    if chars[i] == chars[i].upper():
      chars[i] = chars[i].lower()
    elif chars[i] == chars[i].lower():
      chars[i] = chars[i].upper()
      
  # return the modified list of characters joined as a string
  return ''.join(chars)
      
print SwapCase("Hello World")  

Refactored

def SwapCase(s):
    a = ''
    for i in s:
        if i == i.lower():
            a += i.upper()
        elif i == i.upper():
            a += i.lower()
        else:
            a += i
    return a
print SwapCase(raw_input())

Simplified
def SwapCase(s):
    return(s.swapcase())
print SwapCase(raw_input())

