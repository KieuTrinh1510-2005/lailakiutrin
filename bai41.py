# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:41:09 2024

@author: Student
"""

n = int(input("Nhap so nguyen duong:"))
s = 0
while n < 0 :
    n = int(input("Nhap lai n :"))
for i in range(0, n +1):
    s += 1/(2*i+1)
print("S=",s)