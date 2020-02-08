#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:11:40 2020
Check Vowels in a string
@author: vvbaliga
"""

def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    print(len(final)) 
    print(final) 
      

string = "abcdefghiahkjhfkk"
vowels = "AaeEeIiOoUu"
Check_Vow(string, vowels)
