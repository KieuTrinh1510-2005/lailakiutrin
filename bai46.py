# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 07:32:41 2024

@author: Student
"""
bo_nghiem_nguyen = []
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x+7*y+9*z==979:
                bo_nghiem_nguyen+=[(x,y,z)]
if bo_nghiem_nguyen:
    print(f"{bo_nghiem_nguyen}")
