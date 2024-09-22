# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:33:39 2024

@author: Student
"""
n = int(input("Nhap vao so nguyen duong: "))
while n <= 0 :
    n = int(input("Nhap lai n : "))
s = 0
for i in range (1,n+1):
    s += i
print("S=",s)
