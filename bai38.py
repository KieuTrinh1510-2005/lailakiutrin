# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 09:31:11 2024

@author: Student
"""

n = int(input("Nhap vao n:"))
s = 1
while n <= 0:
    n = int(input("Nhap lai n :"))
for i in range (1, n+1):
    s *= i
print("S=",s)