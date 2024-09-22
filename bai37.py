# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:26:55 2024

@author: Student
"""

n = int(input("Nhap vao so chan: "))
s = 0
while n <=0:
    n = int(input("Nhap lai n :"))
for i in range(2,n+1,2):
    s += i 
print("S=",s)