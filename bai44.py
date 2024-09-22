# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:04:06 2024

@author: Student
"""

n = int(input("Nhap n :"))
s =0
while n < 0:
    n = int(input("Nhap lai n:"))
for i in range (0, n+1):
    s += (2*i+1)/(2*i+2)
print("S=",s)