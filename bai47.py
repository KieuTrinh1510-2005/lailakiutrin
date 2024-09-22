# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 07:43:32 2024

@author: Student
"""

a = []
lon_nhat = 0
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x+7*y+9*z==979:
                tong = x +y+z
                if tong > lon_nhat:
                    lon_nhat= tong
                    a = [(x,y,z)]
if a:
    print(f"{a} voi {x+y+z} = {lon_nhat}")
