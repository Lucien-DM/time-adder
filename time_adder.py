#!/usr/bin/env python3
#Time Adder Version 1.0 - Credit Lucien Di Mattia 2026
list_seconds = []
list_minutes = []
while True:
    x = input("minutes | input finish to end $ ") 
    if x == "finish":
        break
    y = input("seconds $ ")
    try:
        int(x)
        int(y)
    except TypeError:
        print("Input must be an interger! Try again.")
    else:
        if int(x) >= 0 and int(y) >= 0:
            list_seconds.append(int(y))
            list_minutes.append(int(x))
        else:
            print("Input cannot be negitive! Try again.")

list_minutes.append(sum(list_seconds) // 60)
int_seconds = sum(list_seconds) % 60
int_minutes = sum(list_minutes)

print("TOTAL SUM (min:sec)")
print(f"{int_minutes}:{int_seconds}")
