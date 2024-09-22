# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:24:38 2024

@author: Student
"""

n = int(input("Nhap vao so nguyen duong:"))
s = 0
while n <= 0 :
    n = int(input("Nhap lai n :"))
for i in range (1,n+1):
    s += i**2
print("S = ", s)