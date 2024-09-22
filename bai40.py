# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:56:57 2024

@author: Student
"""

n = int(input("Nhap vao n :"))
s = 0 
while n <= 0:
    n = int(input("Nhap lai n :"))
for i in range(1, n+1):
    s += 1/(2*i)
print("S=",s)