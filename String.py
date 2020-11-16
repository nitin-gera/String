# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:46:40 2018

@author: nitingera
"""

message="i am learning Python! I AM ALREADY AN EXPERT PROGRAMMER"

print(str.capitalize(message))
print(message[:1] + message[1:])
print(message.center(100, "*"))
print("Count of i = ", message.count('i', 0, 10))
print(message.find("AM"))
print(message.find("bdjs"))

dt_group=["deepika", "kranti", "rupesh", "nitin", "devesh", "neha", "anu"]
teams="deepika, kranti, rupesh, nitin, devesh, neha, anu"
print(dt_group)

sep="#"
joined = sep.join(dt_group)
print(joined)

print(len(message))

print(teams.split(","))