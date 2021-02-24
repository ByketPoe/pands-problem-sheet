# weekday.py
# The purpose of this program is to 
# author: Emma Farrell

# Write a program that outputs whether or not today is a weekday.

# (You will need to search the web to find how you work out what day it is)
# USE DATETIME MODULE

# An example of running this program on a Thursday is given below.

# $ python weekday.py
# Yes, unfortunately today is a weekday.


# An example of running it on a Saturday is as follows:

# $ python weekday.py
# It is the weekend, yay!

import datetime

now = datetime.datetime.now()
# if you do %w instead of %A, will return number corresponding to day 0 = Sun, 6 = Saturday etc
print(now.strftime("%A"))