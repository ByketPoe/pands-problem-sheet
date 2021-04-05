# es.py
# The purpose of this program is to count the number of times the letter "e" appears in a text file.
# I decided to count every "e" in the file and not to differentiate between upper and lowercase letters.
# author: Emma Farrell

# The fileinput module is imported and aliased as fi.
# This is required to allow us to parse the file that is input on the terminal when this program is run.
# The sys moduls is imported. This will be used to check that the name of the file was input on the terminal.
import fileinput as fi
import sys  

# Since adding will be a repeated function for adding the number of "e"s, I decided to create a function to do this.
def doAddOne(num):
    num += 1
    return num


# A try/except exception handler is used to attempt to execute the code assuming the file name exists.
# If it does not, the code will skip to the except statement and inform the user that the file does not exist, or that the name is wrong.
# If the file exists, the code block under "try" will be executed and the code block under "except" will be ignored.
try:
    # The .input() function from the fileinput module takes in all of the lines of the second file specified in the terminal (skipping over the python file itself).
    # These lines are assigned to a variable. This method means that we do not need to use the 'with open()' as shown in lectures.
    fileToParse = fi.input()

    # The code needs to check and make sure a file name was input at the terminal. 
    # If no filename is input, the .input() function defaults to sys.stdin, allowing the user to input text from the terminal.
    # I found this difficult to use, so decided to use error handling to prevent this from happening.
    # Another option was to pass a filename to use as a default into the .input() function. 
    # I didn't like this, as it meant that incorrect file names input on the terminal would not throw an error.

    # The second input in the terminal can be accessed by using sys.argv[1:]. 
    # In our case, this is the text file we will be using to count the 'e's.
    # The any() function takes in an iterable value and returns a boolean value, True if there is anything in the iterable, otherwise False.
    # An if statement checks if the any() function returns True or False.  
    if not any(sys.argv[1:]):
        # If any() returns False, 'raise' will raise an exception. 
        # The code will skip down to the StopIteration except clause below and execute the code within it. 
        raise StopIteration

    # I tried to use the next() function to throw an exception without having to raise it myself, but it did not work. 
    # The next() function returns the next item in an iterable, I was hoping it would return None and throw an exception.

    # A variable to track the number of "e"s is created and set to 0.
    count = 0
    # A for loop iterates through each line in the file stored in the variable fileToParse. 
    # The variable "line" stores the current line in the file.
    # This updates to the next line on each iteration of the for loop. 
    for line in fileToParse:
        # Another for loop is nested in the first for loop. 
        # This nested loop enables me to access each individual letter in the line.
        # This iterates through the letters in the line stored in the variable "line".
        # The variable "letter" stores the current letter in the line.
        # This updates to the next letter on each iteration of the for loop. 
        for letter in line:
            # To be able to count all "e"s including uppercase ones, I decided to convert all of the letters to lowercase before checking if they are equal to "e".
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

except StopIteration:
    # This code executes if a stop iteration is thrown, most likely by the if statement used above.
    # Usually, StopIterations are thrown when there are no further items produced by an iterator.
    print('You need to enter the name of a text file into the terminal when you run this program.')

except IOError:
    # This code only executes if the code under the "try" fails and throws an input/output error. Otherwise, it is ignored.
    # The print statement informs the user of what the issue is. 
    # The .filename() function from the fileinput module is used to get the name of the file, 
    # as fileToParse is an object and cannot output the name of the file in a way that is useful to the user.
    print("The file {} does not exist, or the file name is incorrect.".format(fi.filename()))