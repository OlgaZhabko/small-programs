#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''This program solves an input line for line sudoku correcting wrong input'''
from time import process_time

def asksudo():
    '''asks to input a sudoku line for line correcting wrong input'''
    sudolist=[]
    for line in range(9):
        sudoline=input(f'Input line {line+1} of your SUDOKU (digits 1-9 and 0 or any other symbol for empty spaces): ')
        sudoline=list(sudoline)
        # checking if the length is 9 and adding '0' to the end of the linelist if it is less
        if len(sudoline)<9:
            sudoline+=['0']*(9-len(sudoline))
        #checking if all the characters in the list are digits and changing to '0' othersise
        for i in range(9):
            if sudoline[i] not in '0123456789':
                sudoline[i]='0'
        sudolist.append(list(map(int, sudoline)))
    return sudolist
        
def solve(sudo):
    '''solving sudoku'''
    sol=[[y for y in x] for x in sudo]
    res = solv_step(sol)
    if res:
        return sol
    
def solv_step(sol):
    '''function tries to solve a sudoku'''
    while True:
        min_pos=None    # var to save a position with minimum variants
        for ri in range(9):
            for ci in range(9):
                if sol[ri][ci]:
                    continue
                else:
                    pv=get_poss_val(ri, ci, sol)
                    pv_count=len(pv) 
                    if not pv_count:
                        return False
                    if pv_count==1: # if the only possible value found for the position
                        sol[ri][ci], = pv # we save the value in the empty position
                    if not min_pos or len(min_pos[1])>pv_count: # we save the minimum value of min_pos
                            min_pos=(ri,ci), pv
        if not min_pos: #if there are no empty positions
            return True
        elif len(min_pos[1])>=2:
            break
    # if there are no more empty positions with the only possible value
    (r, c), z = min_pos
    for v in z:
        sol_copy=[[y for y in x] for x in sol] 
        sol_copy[r][c]=v
        if solv_step(sol_copy): 
            for r in range(9):
                for c in range(9):
                    sol[r][c]=sol_copy[r][c] 
            return True 
        
def get_block_val(ri, ci, sud):
    '''function finds all existing values in the block'''
    rst = 3*(ri//3)
    cst = 3*(ci//3)
    return {sud[rst+x][cst+y] for x in range(3) for y in range(3)}

def get_poss_val(ri, ci, sud):
    '''function finds possible value/values for an empty position with indexes [ri][ci]'''
    res = {1,2,3,4,5,6,7,8,9} 
    res = res - set(sud[ri])             # excluding existing row digits
    res = res - {ri[ci] for ri in sud}   # excluding existing column digits
    res = res - get_block_val(ri,ci,sud) # excluding existing block digits with function 'get_block_val'
    return res
def printsud(sud):
    '''function outputs sudoku on the screen'''
    print('+-------+-------+-------+')
    for k in range(9):
           print('|', sud[k][0], sud[k][1], sud[k][2], 
                 '|', sud[k][3], sud[k][4], sud[k][5],
                 '|', sud[k][6], sud[k][7], sud[k][8], '|')
           if k%3==2:
               print('+-------+-------+-------+')

sudolist=asksudo()
print(f'We are starting to solve this Sudoku: ')
printsud(sudolist)
t0=process_time()
res = solve(sudolist)
t=process_time() - t0
if res:
    print(f'Sudoku has been solved for {t} econds')
    printsud(res)
else:
    print(f'Sudoku has not been solved for {t} seconds')

