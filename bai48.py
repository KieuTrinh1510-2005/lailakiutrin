# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 07:39:01 2024

@author: Student
"""

ds =[]
nho_nhat=979
for x in range (1,490):
    for y in range (1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                tong = x + y +z
                if tong < nho_nhat:
                    nho_nhat = tong
                    ds += [(x,y,z)]
if ds:
    print(f"{ds} voi {x+y+z}={nho_nhat}")
    
                