#!/usr/bin/env python3
#Time Adder Version 1.1.2 - UNSTABLE BUILD - Credit Lucien Di Mattia 2026
import sys
import time
VERSION = "V1.1.2"
UNSTABLE = True

# Debug Toggle

if len(sys.argv) >= 2:
    if sys.argv[1] == "--debug":  
        DEBUG = True
    else:
        DEBUG = False
else: 
    DEBUG = False 

# Logging
class Logger:
    def info(self, message):
        print(f"{time.time()} - INFO - {message}")
    def warn(self, message):
        print(f"{time.time()} - WARN - {message}")
    def error(self, message):
        print(f"{time.time()} - ERROR - {message}")

class DummyLogger: #stops the program from erroring due to an undefined log
    def info(self, message):
        pass
    def warn(self, message):
        pass
    def error(self, message):
        pass

if DEBUG:
    log = Logger()
else:
    log = DummyLogger()

if UNSTABLE:
    print("THIS IS AN UNSTABLE BUILD")
    log.warn(f"VERSION {VERSION} IS AN UNSTABLE BUILD")



#Init Lists
seconds_list = []
minutes_list = []
hours_list = []

#Some Debug info
log.info(f"Time adder {VERSION}")
log.info("Program started execution")
log.warn("Debugging is Enabled!")
log.warn("Logging is Enabled!")

# Mode assignment

while True: 
    print("Valid modes are hm, ms, hms. hm for adding hours and minutes, ms for minutes and seconds, and hms for hours, minutes, and seconds.")
    mode = input("Mode $ ")
    if mode == "ms" or mode == "hm" or mode == "hms":
        log.info(f"Mode selected as '{mode}'")
        break
    else:
        log.warn(f"Mode '{mode}' is Invalid!")
        print("Invalid Mode!")

# Validation

def validate_positive_int(x):
    #Outputs:
    #0 if OK
    #1 if non int
    #2 if negitive
    try:
        int(x)
    except ValueError:
        log.warn(f"Value '{x}' is non integer! Should be interger.")
        return 1 #Non Int
    else: 
        if int(x) >= 0:
            log.info(f"Positive Interger '{x}' is OK")
            return 0 #OK
        else:
            log.warn(f"Value '{x}' is negitive! Should be postive.")
            return 2 #Not Positive

# Inputs

def input_hours():
     log.info("Inputting Hours")
     input_hour = input("Input Hours | Input 'finish' to end")
     if input_hour == "finish":
         return "finish"
     else:
        if validate_positive_int(input_hour) == 0:
            return input_hour
        elif validate_positive_int(input_hour) == 1:
            return -1 #Non Int Error
        elif validate_positive_int(input_hour) == 2:
            return -2
        else:
            log.error("Unexpected value returned from function 'validate_positive_int' - line 81")
            sys.exit

def input_minutes():
     log.info("Inputting Minutes")
     input_minute = input("Input Minutes | Input 'finish' to end")
     if input_hours == "finish":
         return "finish"
     else:
        if validate_positive_int(input_minute) == 0:
            return input_minute
        elif validate_positive_int(input_minute) == 1:
            return -1 #Non Int Error
        elif validate_positive_int(input_minute) == 2:
            return -2
        else:
            log.error("Unexpected value returned from function 'validate_positive_int' - line 81")
            sys.exit

def input_seconds():
     log.info("Inputting Seconds")
     input_hour = input("Input Seconds | Input 'finish' to end")
     if input_hour == "finish":
         return "finish"
     else:
        if validate_positive_int(input_second) == 0:
            return input_hour
        elif validate_positive_int(input_second) == 1:
            return -1 #Non Int Error
        elif validate_positive_int(input_second) == 2:
            return -2
        else:
            log.error("Unexpected value returned from function 'validate_positive_int' - line 81")
            sys.exit()

#Prosessing and output

def minutes_and_seconds(seconds_in_list, minute_in_list):
    seconds_out = sum(seconds_in_list) % 60
    minutes_in_list.append(sum(seconds_in_list) // 60)
    minutes_out = sum(minutes_in_list)
    print("TOTAL OUT! (minutes:seconds)")
    print(f"{minutes_out}:{seconds_out}")
    log.info("Done!")
    sys.exit()

def hours_and_minutes(minutes_in_list, hours_in_list):
    minutes_out = sum(minutes_in_list) % 60
    hours_in_list.append(sum(minutes_in_list) // 60)
    hours_out = sum(hours_in_list)
    print("TOTAL OUT! (hours:minutes)")
    print(f"{hours_out}:{minutes_out}")
    log.info("Done!")
    sys.exit()

def hours_minutes_and_seconds(hours_in_list, minutes_in_list, seconds_in_list):
    seconds_out = sum(seconds_in_list) % 60
    minutes_in_list.append(sum(seconds_in_list) // 60)
    minutes_out = sum(minutes_in_list) % 60
    hours_in_list.append(sum(minutes_in_list) // 60)
    hours_out = sum(hours_in_list)
    print("TOTAL OUT! (hours:minutes:seconds)")
    print(f"{hours_out}:{minutes_out}:{seconds_out}")
    log.info("Done!")
    sys.exit()

# MAIN

if mode == "hms":
    while True:
        hour = input_hours()
        if hour == "finish":
            break
        elif hour == -1: #Non Int Error
            print("Input must be an interger!")
        elif hour == -2: #Negitive Value Error
            print("Input must be Positive!")
        else:

            minute = input_minutes()
            if minute == "finish":
                break
            elif hour == -1: #Non Int Error
                print("Input must be an interger!")
            elif minute == -2: #Negitive Value Error
                print("Input must be Positive!")
            else:

                second = input_seconds()
                if second == "finish":
                    break
                elif hour == -1: #Non Int Error
                    print("Input must be an interger!")
                elif minute == -2: #Negitive Value Error
                    print("Input must be Positive!")
                else:

                    hours_list.append(int(hour))
                    minutes_list.append(int(minute))
                    seconds_list.append(int(second))
    hours_minutes_and_seconds(hours_list, minutes_list, seconds_list)

if mode == "hm":
    while True:
        hour = input_hours()
        if hour == "finish":
            break
        elif hour == -1: #Non Int Error
            print("Input must be an interger!")
        elif hour == -2: #Negitive Value Error
            print("Input must be Positive!")
        else:

            minute = input_minutes()
            if minute == "finish":
                break
            elif hour == -1: #Non Int Error
                print("Input must be an interger!")
            elif minute == -2: #Negitive Value Error
                print("Input must be Positive!")
            else:

                hours_list.append(int(hour))
                minutes_list.append(int(minute))
    hours_and_minutes(hours_list, minutes_list)

if mode == "ms":
    while True:
            minute = input_minutes()
            if minute == "finish":
                break
            elif hour == -1: #Non Int Error
                print("Input must be an interger!")
            elif minute == -2: #Negitive Value Error
                print("Input must be Positive!")
            else:
                second = input_seconds()
                if second == "finish":
                    break
                elif hour == -1: #Non Int Error
                    print("Input must be an interger!")
                elif minute == -2: #Negitive Value Error
                    print("Input must be Positive!")
                else:
                   
                    minutes_list.append(int(minute))
                    seconds_list.append(int(second))
    minutes_and_seconds(minutes_list, seconds_list)
