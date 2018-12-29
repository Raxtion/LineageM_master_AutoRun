import timer
import math
import pyautogui as g
import time

def clickKeyDownS():
    g.keyDown("S")

def clickKeyUpS():
    g.keyUp("S")

def clickKeyDownA():
    g.keyDown("A")

def clickKeyUpA():
    g.keyUp("A")

def clickKeyDownW():
    g.keyDown("W")

def clickKeyUpW():
    g.keyUp("W")

def clickKeyDownD():
    g.keyDown("D")

def clickKeyUpD():
    g.keyUp("D")


def GoMove(nIndex, tm1MS):
    if nIndex == 0:
        if True:
            clickKeyDownS()
            tm1MS.timestart(2000)

            nIndex += 1
    elif nIndex == 1:
        if tm1MS.timeup():
            clickKeyUpS()
            #tm1MS.timestart(2000)

            nIndex += 1
    elif nIndex == 2:
        if tm1MS.timeup():
            clickKeyDownA()
            tm1MS.timestart(2000)

            nIndex += 1
    elif nIndex == 3:
        if tm1MS.timeup():
            clickKeyUpA()
            #tm1MS.timestart(2000)

            nIndex += 1
    elif nIndex == 4:
        if tm1MS.timeup():
            clickKeyDownW()
            tm1MS.timestart(2000)

            nIndex += 1
    elif nIndex == 5:
        if tm1MS.timeup():
            clickKeyUpW()
            #tm1MS.timestart(2000)

            nIndex += 1
    elif nIndex == 6:
        if tm1MS.timeup():
            clickKeyDownD()
            tm1MS.timestart(2000)

            nIndex += 1
    elif nIndex == 7:
        if tm1MS.timeup():
            clickKeyUpD()
            #tm1MS.timestart(2000)

            nIndex += 1
    else:
        nIndex = 0

    return nIndex





if __name__ == '__main__':

    nIndex = 0
    T_ = timer.Timer()

    while True:
        nIndex = GoMove(nIndex, T_)


