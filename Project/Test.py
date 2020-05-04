#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:24:00 2020

@author: tengjiaowang
"""

import sys

def read_file():
     fp_FEAR = open("SADNESS.txt","r")
     for line in fp_FEAR.readlines():
         print(line)
     
     
     
     
def main():
    read_file()
if __name__ == "__main__":    
    main()