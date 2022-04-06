#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''the program tests its function vowelremover on a string and outputs the result'''
def vowelremover(stroka):
    '''this function removes all vowels from a string'''
    for v in 'aeouiyAEOUIY':
        stroka=stroka.replace(v, '')
    return stroka
str1='Hello, everybody, I\'m so glad to see you today! Let\'s get started!!!'
print(str1)
print(vowelremover(str1))