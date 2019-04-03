# https://www.coderbyte.com/information/Dash%20Insert
# Difficulty Easy
# Implemented range() and if/and conditional

def DashInsert(str): 

  # convert the string into a list
  # with each element being a single number
  arr = list(str)

  # loop through the list of numbers and add a dash if 
  # the current number and the next number are odd
  # NOTE: to determine if a number is odd we  
  # divide by 2 and check if there is a remainder
  # e.g. 4 / 2 = 0 remainder
  # e.g. 5 / 2 = 1 remainder
  # e.g. 9 / 2 = 1 remainder
  for i in range(0, len(arr)-1):
    if (int(arr[i]) % 2 != 0 and int(arr[i+1]) % 2 != 0):
      arr[i] = arr[i] + '-'
    
  # join the numbers into a final string
  return "".join(arr)

print DashInsert("13568999") 