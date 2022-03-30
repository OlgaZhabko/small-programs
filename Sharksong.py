#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''The program creats a string with the funny "Shark-song", writes it to a text file in directory ProgrammsPython and outputs the song on the screen'''
from os.path import abspath, join
f_path=abspath(join('..', 'ProgrammsPython', 'Sharksong.doc'))
v=''
for relative in ['Baby', 'Mommy', 'Daddy', 'Grandma', 'Grandpa']:
    v+=((relative + ' shark, ' +'doo '*6 +'\n')*3 + relative+ ' shark!\n\n')
v+=(("Let's go hunt, " + 'doo '*6 +'\n')*3 +"Let's go hunt!\n\nRun away,...")
with open(f_path, mode='wt', encoding='UTF-8') as dst:
    print(v, file=dst)
print(v)