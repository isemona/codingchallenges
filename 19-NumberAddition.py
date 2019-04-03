# https://www.coderbyte.com/editor/Number%20Addition:Python
# Difficulty Easy
# Implemented type-casting list and isdigit() method

'''What I like about this that I deleted the unnecessary strings to distill it to just the integers. created a list and added it from there.
Also at first glance I didn't really understand what the function was doing until I broke it down into print statements.'''


def NumberAddition(s): 
    a = ''
    for i in range(len(s)):
        if s[i] in '1234567890':
            a += s[i]
        else:
            a += ' '
    
    a = a.split()
    x = 0
    for i in a:
         x += int(i)
    return x
print NumberAddition(raw_input())


Or better:

def NumberAddition(str): 
  
  # convert the string into a list of characters
  arr = list(str)
  
  # loop through the list and check if each character
  # is a number, if not then replace it with an empty space
  for i in range(0, len(arr)):
    if not arr[i].isdigit():
      arr[i] = ' '
  
  # join the array into a new string and split
  # it into a new list separated by spaces
  # e.g. ['7', '5', '', '', '', '9'] -> ['75', '', '', '', '9']
  onlyNumbers = ''.join(arr).split(' ')
  answer = 0
  
  # add all the remaining numbers
  for i in range(0, len(onlyNumbers)):
    if onlyNumbers[i].isdigit():
      answer += int(onlyNumbers[i])
    
  # return the final answer  
  return answer

print NumberAddition(rawinput())

