#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''This program asks to enter a Roman number and decodes it into an integer. If the entry is wrong it returns 0 or removes wrong symbols, leaving only symbols MDCLXVI'''
romans={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
def decode(numstr):
    res=[romans[l] for l in numstr]
    for i in range(1, len(res)):
        if res[i-1]<res[i]:
            res[i-1]=-res[i-1]    
    return sum(res)
romannumb=input('Enter a Roman number: ')
romannumb=romannumb.upper()
romannumb=''.join([let for let in romannumb if let in 'MDCLXVI'])
print(f'The Arab number for the Roman number {romannumb} is {decode(romannumb)}')     
