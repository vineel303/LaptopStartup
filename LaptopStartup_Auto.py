import AppData.laptopStartup as b
import Settings.Settings as settingsFile
import Settings.List as a
from datetime import datetime

b.getTickTick()

dateTimeObject = datetime.now()
currentDate = dateTimeObject.strftime("%Y%m%d")
currentTime = dateTimeObject.strftime("%H")
currentWeekday = dateTimeObject.weekday()

if int(currentTime) > 2:
    
    with open(settingsFile.lastDateFilePath, "rt") as lastDateFile:
        lastDate = lastDateFile.read()
    with open(settingsFile.lastDateFilePath, "wt") as lastDateFile:
        lastDateFile.write(currentDate)
    
    if currentDate != lastDate:

        #daily 1/2
        b.openApps(a.dailyApps)
        
        #weekly
        for pair in a.weeklyFolders:
            if pair[0] == currentWeekday:
                b.openFolder(pair[1])
        for pair in a.weeklySites:
            if pair[0] == currentWeekday:
                b.openSite(pair[1])
        
        #monthly
        for pair in a.monthlySites:
            if pair[0] == currentDate[6:8]:
                b.openSite(pair[1])
        
        #quarterly
        quarterlyDate = b.translateToQuarterlyDate(currentDate)
        for pair in a.quarterlyFolders:
            if pair[0] == quarterlyDate:
                b.openFolder(pair[1])
        for pair in a.quarterlySites:
            if pair[0] == quarterlyDate:
                b.openSite(pair[1])
        
        #yearly
        for pair in a.yearlySites:
            if pair[0] == currentDate[4:8]:
                b.openSite(pair[1])
        
        #daily 2/2
        b.openSites(a.dailySites)
        b.getMsTeams()
