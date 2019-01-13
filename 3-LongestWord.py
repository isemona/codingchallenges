# https://www.coderbyte.com/information/Longest%20Word
# Difficulty - Easy
# implemented enumerate

def LongestWord(sen): 
    i = 0
    longestWord = ''

    for j, ch in enumerate(sen):
        
        if not ch.isalpha():
            i = j + 1
    
        if len(longestWord) < (j-i+1):
            longestWord = sen[i:j+1]
    
    return longestWord

# keep this function call here  
print LongestWord(raw_input())