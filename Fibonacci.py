#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''This funny program outputs the desired number of Fibonacci numbers (1-1000) beginning with 1 and 1 with the help of a generator'''
class Nfib(object):
    def __init__(self, n=1000):
        self.__n = 1
        self.__fipr=0
        self.__fi = 1
        self.__maxit=n
    def __next__(self):
        if self.__n == 1:
            self.__fi = 1
        else:
            self.__fipr, self.__fi = self.__fi, self.__fi+self.__fipr
        self.__n+=1
        if self.__n >self.__maxit+1:
            raise StopIteration
        return self.__fi
    def __iter__(self):
        return self

while True:
    maxnum=input('Please enter the maximum number of Fibonacci sequence you would like to see (1-1000): ')
    try:
        maxnum=int(maxnum)
        if maxnum<1:
            print(f'The number must be >0 and you entered {maxnum}')
            continue
        elif maxnum>1000:
            print(f'The number must be <=1000 and you entered {maxnum}')
            continue
        else:
            break
    except ValueError:
        print(f'You entered {maxnum} and we need a whole number')

print(f'Here is the Fibonacci sequence of {maxnum} numbers:')
res=list(Nfib(maxnum))

if len(res)>10:
    for i in range(0, (len(res) - len(res)%10), 10):
        print(*res[i:i+10])
    if len(res)%10!=0:
        print(*res[-(len(res)%10):])
else:
    print(*res)