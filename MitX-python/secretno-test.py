#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:49:15 2020

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!

@author: vvbaliga
"""

print ("Please think of a number between 0 and 100!")
low=0
high=100

while True:
    ans=(high+low)//2
    print ("Is your secret number " +str(ans))
    s = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
    
    if s== 'l':
        low =ans
    elif s== 'h':
        high = ans
    elif s== 'c':
        print("Game over. Your secret number was " + str(ans) )
        break
    else:
        print("Bad operand type: Type again")
    
    
