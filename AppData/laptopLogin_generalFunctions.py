from time import sleep
import pygetwindow

def getMsTeams_retry(msTeamsObject, time):
    sleep(time)
    msTeamsObject = pygetwindow.getWindowsWithTitle("Microsoft Teams")
    return msTeamsObject

def getMsTeams():
    msTeamsObject = pygetwindow.getWindowsWithTitle("Microsoft Teams")
    #
    if not msTeamsObject:
        msTeamsObject = getMsTeams_retry(msTeamsObject, 1)
        if not msTeamsObject:
            msTeamsObject = getMsTeams_retry(msTeamsObject, 1)
            if not msTeamsObject:
                msTeamsObject = getMsTeams_retry(msTeamsObject, 1)
    #
    msTeamsObject = msTeamsObject[0]
    msTeamsObject.maximize()
