#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:49:39 2020

@author: vvbaliga
"""
import re 
  
# initializing string   
test_string = "Geeksforgeeks,    is best @# Computer Science Portal.!!!"
  
# printing original string 
print ("The original string is : " +  test_string) 
  
# using regex( findall() ) 
# to extract words from string 
res = re.findall(r'\w+', test_string) 
  
# printing result 
print ("The list of words is : " +  str(res)) 