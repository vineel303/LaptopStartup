import AppData.laptopStartup_main as a

if __name__ == "__main__":
    print("1: Daily. 2: Weekly. 3: Monthly. 4: Quarterly. 5: Yearly.")
    userInput = input("Input: ")
    userInput = list(userInput)
    
    if "1" in userInput:
        a.daily3()
    if "2" in userInput:
        a.weekly3()
    if "3" in userInput:
        a.monthly3()
    if "4" in userInput:
        a.quarterly3()
    if "5" in userInput:
        a.yearly3()
    if "1" in userInput:
        
