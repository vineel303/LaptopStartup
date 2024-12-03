import pygetwindow
from subprocess import run
from AppData.laptopLogin_generalFunctions import *

def openTickTick():
    tickTickObject = pygetwindow.getWindowsWithTitle("TickTick")
    if tickTickObject:
        tickTickObject = tickTickObject[0]
        tickTickObject.restore()
        tickTickObject.activate()
        tickTickObject.maximize()
    else:
        run(r"taskkill /IM TickTick.exe /F")
        run(r"start TickTick://", shell=True)

if __name__ == "__main__":
    openTickTick()
    