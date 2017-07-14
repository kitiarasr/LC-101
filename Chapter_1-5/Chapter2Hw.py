
# !/usr/bin/env python


"""Write a program that calculates the temperature based on how much the dial
has been turned. You should prompt the user for a number of clicks-to-the-right
(from the starting point of 40 degrees). Then you should print the current
temperature.
 By how many clicks has the dial been turned?
>>> -1
The temperature is 89
"""

baseTemp = 40
fullCycle = 50
clicks_str = input("By how many clicks has the dial been turned?")
clicks = int(clicks_str)
result = clicks % fullCycle + baseTemp
print("The temperature is ", result)
