#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:46:41 2020

@author: vvbaliga
"""

#Reverse a String

string1=input("type something:")
string2=str(string1[::-1])
print(string2)


string3=input("type something:")
stringleng=len(string3)
sliced=string3[stringleng::-1]
print(sliced)