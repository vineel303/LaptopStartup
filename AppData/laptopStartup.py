from subprocess import run
from webbrowser import open as openWeb
import pygetwindow
from time import sleep

#functions for opening apps, folders and sites
def openApp(i):
    run(i, shell=True)
def openApps(theList):
    for i in theList:
        openApp(i)

def openFolder(i):
    run(["explorer", i])
def openFolders(theList):
    for i in theList:
        openFolder(i)

def openSite(i):
    openWeb(i)
def openSites(theList):
    for i in theList:
        openWeb(i)

def openPairedApps(theList):
    for pair in theList:
        openApp(pair[1])
def openPairedFolders(theList):
    for pair in theList:
        openFolder(pair[1])
def openPairedSites(theList):
    for pair in theList:
        openSite(pair[1])

#function to get tick tick
def getTickTick():
    tickTickWindow = pygetwindow.getWindowsWithTitle("TickTick")
    if tickTickWindow:
        tickTickWindow = tickTickWindow[0]
        tickTickWindow.restore()
        tickTickWindow.activate()
        tickTickWindow.maximize()
    else:
        run(r"taskkill /IM TickTick.exe /F")
        run(r"start TickTick://", shell=True)

#functions to get ms teams
def getMsTeams_retry(time):
    sleep(time)
    return pygetwindow.getWindowsWithTitle("Microsoft Teams")    
def getMsTeams():
    msTeamsWindow = pygetwindow.getWindowsWithTitle("Microsoft Teams")
    if not msTeamsWindow:
        msTeamsWindow = getMsTeams_retry(1)
        if not msTeamsWindow:
            msTeamsWindow = getMsTeams_retry(1)
            if not msTeamsWindow:
                msTeamsWindow = getMsTeams_retry(1)
    if msTeamsWindow:
        msTeamsWindow = msTeamsWindow[0]
        msTeamsWindow.maximize()

#functions for LaptopStartup_Auto.py only
def translateToQuarterlyDate(oriDate):
    if int(oriDate[4:6]) % 3 == 1:
        newDate = "A" + oriDate[6:8]
    elif int(oriDate[4:6]) % 3 == 2:
        newDate = "B" + oriDate[6:8]
    else:
        newDate = "C" + oriDate[6:8]
    return newDate
