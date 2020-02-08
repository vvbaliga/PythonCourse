#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:13:05 2020

@author: vvbaliga
"""

s = "azcbobobegghakl"
longest = s[0]
current = s[0]
for c in s[1:]:
    if c >= current[-1]:
        current += c
        if len(current) > len(longest):
            longest = current
    else:
        current = c
print ("Longest substring in alphabetical order is:", longest)