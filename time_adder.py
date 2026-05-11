#!/usr/bin/env python3
#Time Adder Version 1.1 - Credit Lucien Di Mattia 2026
list_seconds = []
list_minutes = []
list_hours = []
while True: ## This assigns the mode flag - Will be redesigned in a future version
    print("Valid modes are hm, ms, hms. hm for adding hours and minutes, ms for minutes and seconds, and hms for hours, minutes, and seconds.")
    mode = input("Mode $ ")
    if mode == "ms" or mode == "hm" or mode == "hms":
        break
    else:
        print("Invalid Mode!")
def minutes_seconds():
    while True:
        str_minutes = input("minutes | input finish to end $ ") 
        if str_minutes == "finish":
            break
        str_seconds = input("seconds $ ")
        try:
            int(str_minutes)
            int(str_seconds)
        except ValueError:
            print("Input must be an interger! Try again.")
        else:
            if int(str_minutes) >= 0 and int(str_seconds) >= 0:
                list_seconds.append(int(str_seconds))
                list_minutes.append(int(str_minutes))
            else:
                print("Input cannot be negitive! Try again.")
    list_minutes.append(sum(list_seconds) // 60)
    int_seconds = sum(list_seconds) % 60
    int_minutes = sum(list_minutes)
    print("TOTAL SUM (min:sec)")
    print(f"{int_minutes}:{int_seconds}")

def hours_minutes():
    while True:
        str_hours = input("hours | input finish to end $ ")
        if str_hours == "finish":
            break
        str_minutes = input("minutes $ ")
        try:
            int(str_hours)
            int(str_minutes) 
        except ValueError:
            print("Input must be an interger! Try again.")
        else:
            if int(str_hours) >= 0 and int(str_minutes) >= 0:
                list_minutes.append(int(str_minutes))
                list_hours.append(int(str_hours))
            else:
                print("Input cannot be negitive! Try again.")
    list_hours.append(sum(list_minutes) // 60)
    int_minutes = sum(list_minutes) % 60
    int_hours = sum(list_hours)
    print("TOTAL SUM (hour:minutes)")
    print(f"{int_hours}:{int_minutes}")

def hours_minutes_seconds():
    while True:
        str_hours = input("hours | input finish to end $ ")
        if str_hours == "finish":
            break
        str_minutes = input("minutes $ ")
        str_seconds = input("seconds $ ")
        try:
            int(str_hours)
            int(str_minutes)
            int(str_seconds)
        except ValueError:
            print("Input must be an interger! Try again.")
        else:
            if int(str_hours) >= 0 and int(str_minutes) >= 0 and int(str_seconds) >= 0:
                list_minutes.append(int(str_minutes))
                list_hours.append(int(str_hours))
                list_seconds.append(int(str_seconds))
            else:
                print("Input cannot be negitive! Try again.")
    list_minutes.append(sum(list_seconds) // 60)
    list_hours.append(sum(list_minutes) // 60)
    int_seconds = sum(list_seconds) % 60
    int_minutes = sum(list_minutes) % 60
    int_hours = sum(list_hours)
    print("TOTAL SUM (hour:minutes:seconds)")
    print(f"{int_hours}:{int_minutes}:{int_seconds}")
#This is DEFINITLY not written the best it could be but fuck it we ball.
#MUST FIX BY V1.2
if mode == "ms":
    minutes_seconds()
elif mode == "hm":
    hours_minutes()
elif mode == "hms":
    hours_minutes_seconds()

