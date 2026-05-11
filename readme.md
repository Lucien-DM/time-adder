# Time Adder - Created by Lucien Di Mattia

This program does not require any dependancies and is entirly written in base python.

## Version Roadmap
1.0 - First Release
1.1 - Added Hour handling and mode switching
1.2 - Clean up version 1.1, test, and pull to main branch.
1.3 - Rework UI
*More will be added over time and this program may be rewritten in a compiled lang later*

Current UI:

*Start of execution*
Mode select - hours:minutes - minutes:seconds - hours:minutes:seconds

if hours:minutes:
    ask hours - if finish given, break
    ask seconds
    repeat

elif minutes:seconds:
    ask minutes - if finish given, break
    ask seconds

elif hours:minutes:seconds:
    ask hours - if finish given, break
    ask minutes
    ask seconds

calculate and return total values


