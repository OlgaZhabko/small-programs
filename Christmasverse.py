#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''This programme writes this Christmas poem into a file in 'Data' directory and outputs it on the screen'''
from os.path import abspath, join
f_path=abspath(join('..', 'Data', 'A Christmas poem.txt'))
r=''
o=['First','Second','Third']
o+=[s+'th' for s in ('Four','Fif','Six','Seven','Eigh','Nin','Ten','Eleven','Twelf')]
v=['Twelve drummers drumming,','Eleven pipers piping,','Ten lords a-leaping,','Nine ladies dancing,','Eight maids a-milking,','Seven swans a-swimming,','Six geese a-laying,','Five gold rings,','Four calling birds,','Three French hens,','Two turtle doves, and','A partridge in a pear tree.']
for i in range(12):
    r+='On the '+ o[i]+' day of Christmas\nMy true love sent to me\n'
    r+='\n'.join(v[-i-1:])
    r+='\n\n'
with open(f_path, mode='wt', encoding='UTF-8') as dst:
    print(r[:-3], file=dst)
poemlist=[]
with open(f_path, encoding='UTF-8') as src:
    poemlist=src.readlines()
print(*poemlist)