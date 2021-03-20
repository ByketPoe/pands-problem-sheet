# numberofEs.py
# The purpose of this program is to count the number of times the letter "e" appears in a text file.
# I decided to count every "e" in the file and not to differentiate between upper and lowercase letters.
# author: Emma Farrell

# Since adding will be a repeated function for adding the number of "e"s, I decided to create a function to do this.
def doAddOne(num):
    num += 1
    return num

# The name of the file is assigned to a variable. 
# A variable to track the number of "e"s is created and set to 0.
fileToParse = "fields.txt"
count = 0

# A try/except exception handler is used to attempt to execute the code assuming the file name exists.
# If it does not, the code will skip to the except statement and inform the user that the file does not exist, or that the name is wrong.
# If the file exists, the code block under "try" will be executed and the code block under "except" will be ignored.
try:
    # The file is opened in read mode as the only thing we want to do is count letters. We do not need to change the file itself.
    # The file is a text file, and we only need to see the text in it, so it is opened in text mode. 
    # The opened file is assigned to the variable f.
    with open(fileToParse, "rt") as f:
        # A for loop iterates through each line in the file stored in the variable f. 
        # The variable "line" stores the current line in the file.
        # This updates to the next line on each iteration of the for loop. 
        for line in f:
            # Another for loop is nested in the first for loop. 
            # This nested loop enables me to access each individual letter in the line.
            # This iterates through the letters in the line stored in the variable "line".
            # The variable "letter" stores the current letter in the line.
            # This updates to the next letter on each iteration of the for loop. 
            for letter in line:
                # To be able to cound all "e"s including uppercase ones, I decided to convert all of the letters to lowercase before checking if they are equal to "e".
                # This is done using the .lower() function. 
                # The result of this is stored in the variable "lowletter".
                lowletter = letter.lower()
                # An if statement checks if the current letter is equal to the character "e".
                if lowletter == 'e':
                    # If the statement is true, the count variable is passed to the doAddOne() function.
                    # This will return the current value of count plus one.
                    count = doAddOne(count)

    # The result is printed.
    print("The letter e appears in this file {} times".format(count))

except IOError:
    # This code only executes if they code under the "try" fails. Otherwise, it is ignored.
    # The print statement informs the user of what the issue is. 
    print("The file {} does not exist, or the file name is incorrect.".format(fileToParse))