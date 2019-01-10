# https://www.coderbyte.com/editor/First%20Reverse:Python#

#Difficulty - Easy

def FirstReverse(str): 
	# no built in reverse functions for strings
	# using extended slice syntax (begins and ends at 0)
	# src - https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
    return str[::-1] 

	#You can also do:
	return ''.join(reversed(str))
    
    
# keep this function call here  
print FirstReverse(raw_input())

