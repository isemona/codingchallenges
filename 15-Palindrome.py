# https://www.coderbyte.com/editor/Palindrome:Python#
# Difficulty Easy
# Implemented reversed() method on an iterable object


def Palindrome(str): 

  # first we'll get rid of spaces and make the characters 
  # all lowercase to make it easier to work with
  str = "".join(str.split(" ")).lower()

  # we wrote this reverse code in a previous solution
  rev = ''.join(reversed(str))

  # now it's very easy to check if a string is a palindrome
  if str == rev:
    return "true"
  else:
    return "false"
    
print Palindrome("Never odd or even")

# Mulitiple ways

def Palindrome(s):
    s = ''.join(s.split())
    if s == s[::-1]:
        return 'true'
    return 'false'
print Palindrome(raw_input())