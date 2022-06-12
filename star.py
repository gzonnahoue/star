#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:09:22 2022

@author: mansour
"""

# %% Star program
import argparse


def star(height: int = 0):
    if height == 0:
        return
    else:
        # Upper summit
        for i in range(1, height+1):
            row = " " * (height * 2) + " " * (height - i) + "*" if height != 1 else "   *"
            if i != 1:
                row += " " * (2*(i - 2)+1) + "*"
            print(row)
        # Upper central
        row = "*"*(height*2+1)
        row += " " * (2*(height - 1)-1) if height != 1 else " "
        row += "*"*(height*2+1)
        print(row)
        for i in range(1, height+1):
            row = " " * i + "*" + (height * 2 - i) * " "
            row += " " * (2*(height - 2)+1)
            row += (height * 2 - i) * " " + "*" if height != 1 else "  *"
            print(row)
        # Lower central
        for i in range(height-1, 0, -1):
            row = " " * i + "*" + (height * 2 - i) * " "
            row += " " * (2*(height - 2)+1)
            row += (height * 2 - i) * " " + "*"
            print(row)
        row = "*"*(height*2+1)
        row += " " * (2*(height - 1)-1) if height != 1 else " "
        row += "*"*(height*2+1)
        print(row)
        # Lower summit
        for i in range(height, 0, -1):
            row = " " * (height * 2) + " " * (height - i) + "*" if height != 1 else "   *"
            if i != 1:
                row += " " * (2*(i - 2)+1) + "*" if i != 1 else "  *"
            print(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", type=int, default=1)
    args = parser.parse_args()

    star(args.size)
