# weekday.py
# The purpose of this program is to return a message corresponding the day of the week it is today.
# It reinforces the crushing despair of the week days while celebrating the opportunity given by the weekends.
# author: Emma Farrell

# The datetime module is required for this program, so it is imported.
# It is required to get the current date and to determine what day of the week it is. 
import datetime

# A dictionary is created to associate the days of the week with a number and with the output message I want to associate the day with.
# The numbers are the keys of the dictionary, and can be used to access the value, which in this case is a list.
# The numbers also correspond with the way the datetime module refers to days of the week, where 0 = Sunday, 1 = Monday etc.
# The value is a list because I want to have the name of the day of the week as well as the associated output message. 
daysOfWeek = {"0": ["Sunday", "It is the weekend, yay!"], 
"1": ["Monday", "Yes, unfortunately today is a weekday"], 
"2": ["Tuesday", "Yes, unfortunately today is a weekday"], 
"3": ["Wednesday", "Yes, unfortunately today is a weekday"], 
"4": ["Thursday", "Yes, unfortunately today is a weekday"], 
"5": ["Friday", "Yes, unfortunately today is a weekday"], 
"6": ["Saturday", "It is the weekend, yay!"]}

# The .now() function is called from the datetime module to get the current day, date and time. The result is assigned to the variable "now".
now = datetime.datetime.now()
# The .strftime function is used to get the day of the date stored in the variable "now".
# The argument "%w" tells the function that I want the result to be a number (as a string) corresponding to the day of the week (where 0 = Sunday, 1 = Monday etc).
# I could get the function to return the full name of the day by passing in %A.
day = now.strftime("%w")

# I use the result stored in the variable "day" as a key to refer to the corresponding value in the dictionary "daysOfWeek".
# I need to use the index of the list stored in the dictionary value to get the output message I want, it is the second item in the list, so [1].
# The output message is assigned to the variable "result". 
result = daysOfWeek[day][1]

# The result is printed.
print(result)
