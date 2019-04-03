# https://www.coderbyte.com/editor/Alphabet%20Soup:Python#
# Difficulty Easy
# Implemented the sorted() method which takes an iterable to sort; stored this into a variable to return value. 

def AlphabetSoup(str): 

  # convert the string into a list of characters
  chars = list(str)

  # sort the list in alphabetical order
  sortedChars = sorted(chars)
  
  # return the newly joined string
  return "".join(sortedChars)
    
print AlphabetSoup(raw_input())