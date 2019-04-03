# https://www.coderbyte.com/editor/Ex%20Oh:Python#
# Difficulty Easy
# Implemented the filter function from Python list comprehension 

def ExOh(str): 

  # we split the string with the separator being
  # the x's and o's and compare them

  # this returns a string containing only o's
  x = "".join(str.split("x"))

  # this returns a string containing only x's
  o = "".join(str.split("o"))

  # see if their lengths are equal
  if len(x) == len(o):
    return "true"
  else:
    return "false"
    
print ExOh("xooox")  


or 

def ExOh(str): 

  # split the string into a list
  arr = list(str)

  # create a new list of x's by using the filter function
  # from Python list comprehension
  x = [char for char in arr if char == 'x']

  # because we know the string can only contains x's and o's
  # we can subtract the length of our new array of x's from 
  # arr and that will leave us with the number of o's
  o = len(arr) - len(x)

  # see if their lengths are equal
  if len(x) == o:
    return "true"
  else:
    return "false"
    
print ExOh("xooox")  

or 

def ExOh(s):
    if s.count('x') == s.count('o'):
        return 'true'
    return 'false'
print ExOh(raw_input())