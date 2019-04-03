# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/submissions/code/91395744
# Difficulty Easy 
# Additive Persistence
# Created a dictionary 
# Feb 6

# split the input into a list 
# add each item in the list place that sum into a total accumulator
# put a counter here at the end as well to keep track of the sum

# if the total sum length is greater than 2
# split the sum into a new list 
# add each item in the new list
# else break



def sum_digits(num):
    return sum([int(i) for i in str(num)])


def num_digits(num):
    return len(str(num))
    
    
def oldAdditivePersistence(num): 
    # if num_digits(num) == 1:
    #     return 0
    
    counter = 0
    temp = num
    
    while num_digits(temp) > 1:
        temp = sum_digits(temp) 
        counter += 1
    
    return counter
    
def AdditivePersistence(num): 
    counter = 0
    temp = num
    while len(str(temp)) > 1:
        temp = sum([int(i) for i in str(temp)]) 
        counter += 1
    return counter
    
# keep this function call here  
print AdditivePersistence(raw_input())  


  