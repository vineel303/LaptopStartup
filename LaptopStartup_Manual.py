import AppData.laptopStartup as b
import Settings.List as a

print("1: Daily. 2: Weekly. 3: Monthly. 4: Quarterly. 5: Yearly.")
userInput = list(input("Input: "))

if "1" in userInput:
    b.openApps(a.dailyApps)
    b.openSites(a.dailySites)

if "2" in userInput:
    b.openPairedFolders(a.weeklyFolders)
    b.openPairedSites(a.weeklySites)

if "3" in userInput:
    b.openPairedSites(a.monthlySites)

if "4" in userInput:
    b.openPairedFolders(a.quarterlyFolders)
    b.openPairedSites(a.quarterlySites)

if "5" in userInput:
    b.openPairedSites(a.yearlySites)

if "1" in userInput:
    b.getMsTeams()
