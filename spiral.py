#!/usr/bin/env python3
# -*-coding: UTF-8 -*-
''''this program prints a numeric spiral n x m'''

def print_matrix(matr, width):
    '''this function outputs the matrix with a given width'''
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            print(str(matr[i][j]).ljust(width), end = '')
        print()
    
print('Enter size of the matrix, two whole numbers for number of rows and number of columns: ')
while True:
    try:
        n, m = (int(x) for x in input().split())
        break
    except:
        print('You entered wrong values. Please enter two whole numbers: ')


count = 1
res = [[0 for i in range(m)] for j in range(n)]

minim = min(n, m)

for k in range(minim//2):
    for i in range(k, m-k-1):
        res[k][i] = count
        count+=1
    for j in range(k, n-k-1):
        res[j][m-1-k] = count
        count+=1
    for i in range(m-1-k, k, -1):
        res[n-1-k][i] = count
        count+=1
    for j in range(n-1-k, k, -1):
        res[j][k]=count
        count+=1
        
if n<=m and n%2==1:
    for j in range(m):
        if res[n//2][j] == 0:
            res[n//2][j] = count
            count+=1
elif m<n and m%2==1:
    for j in range(n):
        if res[j][m//2] == 0:
            res[j][m//2] = count
            count+=1
        
print_matrix(res, 5)
