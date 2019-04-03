12-VowelCount
# https://www.coderbyte.com/editor/Vowel%20Count:Python
# Difficulty Easy
# Implemented list comprehension/generator

def VowelCount(str): 

    # code goes here 
    # input - str
    # output - number
    # data structure - looping through a list to count how many vowels
    
    new_list = [vowel for vowel in str if vowel in 'aeiou' or vowel in "AEIOU"]
    
    return len(new_list)
    # for i in str:
    #     if i in 'aeiou' or i in 'AEIOU':
    #         counter += 1
    
    # return counter
    
    
# keep this function call here  
print VowelCount(raw_input())