# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:32:06 2020

@author: Lenovo
"""
#%%

## 1

for i in range(2000,3201):
    if i % 7 == 0 and i % 5 !=0:
        print(i)
#%%

## 2

First_Name = str(input())
Last_Name = str(input()) 

Name = First_Name+' '+Last_Name

print(Name[::-1])

#%%

##3

Diameter = 12

volume = (4/3)*3.14*((Diameter/2)**3)

print(volume)
       
