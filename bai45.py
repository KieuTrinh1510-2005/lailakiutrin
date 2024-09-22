# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 10:07:46 2024

@author: Student
"""
n = int(input("Nhap vao n :"))
x = float(input("Nhap vao x:"))
s = 0
while n <= 0:
    n = int(input("Nhap lai n :"))
for i in range (1,n+1):
    s += (x**i)/(i)
print("S=",s)
