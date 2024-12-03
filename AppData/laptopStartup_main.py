from subprocess import run
from webbrowser import open as openWeb
import Settings.SitesFoldersApps as a

def openSites(sites):
    for i in sites:
        openWeb(i)

def openFolders(folders):
    for i in folders:
        run(["explorer", i])

def openApps(apps):
    for i in apps:
        i = i + "://"
        run(["start", i])

def daily3():
    openApps(a.dailyApps)
    openSites(a.dailySites)

def weekly3():
    openFolders(a.weeklyFolders)
    openSites(a.weeklySites)

def monthly3():
    openSites(a.monthlySites)

def quarterly3():
    openFolders(a.quarterlyFolders)
    openSites(a.quarterlySites)

def yearly3():
    openSites(a.yearlySites)
