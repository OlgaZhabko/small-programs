#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''this program converts any integer into any n-ary system and return the result as a string'''

from string import ascii_uppercase

def encode(number: int, system: int) -> str:
    '''Converts an integer into a n-ary system.

    Parameters:
        number (int): the given number
        system (int): system-nary number system into which the number is being encoded

    Returns:
        the encoded  into system-nary system number as a string
        if system > 10 uppercase letters of the latin alphabet are used
    '''

    res = ''
    while number>0:
        rest = number%system
        if rest>10: rest=ascii_uppercase[rest - 10]
        res = str(rest) + res
        number//=system
    return res

if __name__ == '__main__':
    print(encode(2225, 25))
    print(encode.__doc__)