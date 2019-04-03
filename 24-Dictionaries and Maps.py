# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/submissions/code/91395744
# Difficulty Easy 
# Dictionaries and Maps
# Created a dictionary 
# Feb 3

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# explain what each component will do

# Read input and assemble Phone Book
t = int(input())
phoneBook = {}
for _ in range(t):
    contact = input().split( )
    phoneBook[contact[0]] = contact[1]

# Process Queries  
lines = sys.stdin.readlines()
for i in lines:
    name = i.strip() # there might be extra spaces; the code is not optimal without .strip() method
    if name in phoneBook:
        print(name + '=' + phoneBook[name])
    else:
        print("Not found")