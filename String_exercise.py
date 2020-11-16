# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:12:23 2018

@author: nitingera
"""

poem = "Twinkle twinkle little star"
poem += "how i wonder what you are"
poem += "up above the world so high"
poem += "like a diamond in the Sky"

print(poem)

line = 1
char = 0

while(char < len(poem)):
    if(poem[char] != "\n"):
        curr_char = poem[char]
        if(curr_char.isupper() == True):
            print("Line:", line, "char:", char, curr_char, "Capital")
        else:
            print("Line", line, "char", char, curr_char)
    
    char += 1
