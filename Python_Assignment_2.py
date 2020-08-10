# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:36:36 2020

@author: Lenovo
"""
#%%

## Assignment 01
for i in range(5):
    print('*' * (i+1))

for i in range(4,-1,-1):
    print('*' * (i))
      
    
#%%
## Assignment 01
m1 = []
for i in range(5):
    a = []
    for j in range(5):
        if j-i <= 0:
            a.append('*')
        else:
            a.append(' ')
    m1.append(a)

for i in range(5):
    for j in range(5):
        print(m1[i][j],end ='')
    print()

m2 = []


for i in range(4):
    a1 = []
    for j in range(5):
        if j+i <= 3:
            a1.append('*')
        else:
            a1.append(' ')
    m2.append(a1)

for i in range(4):
    for j in range(5):
        print(m2[i][j],end ='')
    print()            
            
#%%
    
## Assignment 02
    
s = str(input())
print(s[::-1])

#%%

##Assignment 02

s = str(input())
s_rev = []
for i in range(len(s)-1,-1,-1):
    s_rev.append(s[i])
    
print(''.join(s_rev))

            
