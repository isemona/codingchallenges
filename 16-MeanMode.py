# https://www.coderbyte.com/editor/Arith%20Geo:Python#
# Difficulty Easy
# Implemented a hash table

def MeanMode(arr): 

  # calculate the mean by dividing the sum by the
  # number of elements in the list
  mean = sum(arr) / len(arr)
  
  # the table that will contain each number as the key
  # and the number of times it occurs as the value
  # e.g. {"5": 1, "3": 3, "1": 1}
  table = {}
  
  # loop through each number in the list
  # see if this number already exists in table
  # if so add 1 to the count, if not set count = 1
  for i in range(0, len(arr)):
    number = arr[i]
    if number in table:
      table[number] += 1
    else:
      table[number] = 1
      
  # setup a new dictionary that will store the number with the highest count
  answer = {"number": '', "count": 0}
  
  # get the mode by determining what number appears most often in the table 
  for n in table:
    if (table[n] > answer["count"]):
      answer["count"] = table[n]
      answer["number"] = n
      
  if answer["number"] == mean:
    return 1
  else:
    return 0
    
print MeanMode(raw_input())