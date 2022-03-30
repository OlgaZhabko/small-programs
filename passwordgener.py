#!/usr/bin/env python3
#-*- encoding:utf-8 -*-
'''this programme generates a password of desired length and contains letters, digits and special symbols.'''
from random import choice, shuffle

def gener_a_password(leng=8, numb=1, spec=1):
    '''generates a password of given length, contains given number of digits  and special symbols. Takes three arguments(leng=1, numb=1, spec=1)'''
    passw=[]
    for i in range(leng-numb-spec):
        passw.append(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if numb:
        for i in range(numb):
            passw.append(choice('1234567890'))
    if spec:
        for i in range(spec):
            sp=choice('!?_@#$%&*~')
            if sp not in passw:
                passw.append(sp)
            else:
                passw.append(choice('!?_@#$%&*~'))
    start=passw[0]
    passw=passw[1:]
    shuffle(passw)
    passw.insert(0, start)
    return ''.join(passw)

print(f'A password containing 6 letters, 1 digit  and 1 special symbol: \t{gener_a_password(8,1,1)}')
print(f'A password containing 7 letters, 2 digits and 1 special symbols:\t{gener_a_password(10,2,1)}')
print(f'A password containing 7 letters, 2 digits and 2 special symbols:\t{gener_a_password(11,2,2)}')
print(f'A password containing 8 letters, 2 digits and 2 special symbols:\t{gener_a_password(12,2,2)}')
print(f'A password containing 8 letters, 3 digits and 3 special symbols:\t{gener_a_password(14,3,3)}')
