from datetime import datetime
import AppData.laptopStartup_main as a
import Settings.Settings as s

if __name__ == "__main__":
    #get current date
    dateToday = datetime.now()
    dateToday_YYMD = dateToday.strftime("%Y%m%d")
    dateToday_W = dateToday.weekday()
    #get last date
    with open(s.lastDateFilePath, "rt") as lastDateFile:
        lastDate = lastDateFile.read()
    with open(s.lastDateFilePath, "wt") as lastDateFile:
        lastDateFile.write(dateToday_YYMD)
    