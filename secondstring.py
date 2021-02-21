# secondstring.py
# The purpose of this program is to take in text and return every second letter in reverse order.
# author: Emma Farrell

# The user is asked for some text. 
# The input function is used to request this text and take it in.
# The text is passed to the variable inputText.
# Technically, according to the Whirlwind Tour of Python book, inputText is a pointer pointing to the value, as opposed to inputText storing the value.
# But let's not get too carried away.
inputText = input("Please enter your sentence: ")

# String Slicing is used to remove every second letter from the string and to reverse the string. 
# The first input tells the program which index to start with, the second index denotes which index to end with.
# In this case, we want all characters from the string to be take into account, so these are left blank.
# The last input tells the program how many indexes to step over each time, so 1 would step through one at a time, 3 would take every 3rd character etc.
# In our case, we want every second character, so the input is 2. 
# The minus in front of the 2 reverses the direction in which the string is sliced, starting at the end and moving backwards. 
# This returns the reverse of every second character in the string. 
result = inputText[::-2]

# The result is output using the print() function. 
print(result)