# pands-problem-sheet
Submission for PandS problem sheets

Week 2 bmi.py 
    Explanation of code:
        This program works by taking in height and weight measurements from the user and using them to calculate bmi. The input and print functions and casting data to desired data type (in this case, float) have been covered in lecture material. The round function was found on W3 schools at the link in the reference. This function works by taking in the number to be rounded as well as the number of decimal places that is required: 
            round(<number>, <number of decimal places>). 
        These calculations work by assigning the values inputted and calculated to variables, which has been covered in lecture material. 
        The formula for BMI is weight divided by height squared, and is taken from the link in the references.
    References:
        Round function:     https://www.w3schools.com/python/ref_func_round.asp
        BMI formula:        https://www.wolframalpha.com/input/?i=bmi
        

Week 3 secondstring.py
    Explanation of code:
        Strings are an example of something that is iterable i.e. a sequence of data. Iterable data types use numbers called indexes to refer to the position of the data within the sequence, starting at 0. When referring to indexes in reverse, the index starts at -1. 
        
        This program uses string slicing to return every second character of a string in reverse. String slicing uses the indexes of a string to determine what characters to remove and which to keep, and were found at the links below. 
        String slicing works in the following way, where stringVariable contains a string:
            stringVariable[<start>:<stop>:<step>]
        
        An iterable (in this case, a string) followed by square brackets means that the indexes of the iterable are being used to refer to the contents. Slicing uses the indexes to determine where to start, stop and step through. So for example someString[3:8:2] would return every second character from the string from index 3 up to (but not including) index 8. A minus number reverses the direction of the indexes. 
        
        In this program, string slicing is used to return every second character in a string in reverse order.
    References:
        Slicing Strings:    https://www.w3schools.com/python/python_strings_slicing.asp
                            https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3


Week 4 collatz.py
    Explanation of code:
        The sample output in the question shows the numbers as integers, so the input number is cast as an integer and integer division is used in the calculation. A while loop checks the current value of the input initially and after each time the calculations are done. The while loop terminates once the value reaches 1. 
        
        Within the while loop, an if statement checks if the value is even or odd. The remainder (modulus [%]) of the input value when divided by 2 is calculated to determine if it is odd or even. If it is even, the remainder will be 0, otherwise it is odd. The if statment executes the calculation to divide the value by 2 if it is even, otherwise the else statement executes the multiplication by 3 and addition of 1 to the value. Because there are only two possible outcomes from the if statement (the value is odd or even) there is no need to check again using an elif statement. 
        
        By adding 1 to the odd value, the value will always eventually reduce down to 1 by being divided by 2 on the next iteration as it will be even. This ensures the while loop does not execute infinitely. 
        
        The sample output given in the question showed the calculated values in a row on one line. I decided the best way to replicate this would be to create a list to hold all of the values in. The initial value entered is added to the list when it is initially created. After the calculations are done on the value, the new value is also added to the list at the end of every iteration of the loop. This list is then printed at the end to show the results.
    References:


Week 5 weekday.py
    Explanation of code:
        The datetime module is used for two functions in the code; the function to obtain the current date and the function to convert it to show the day of the week. The code uses a dictionary to store the days of the week and a corresponding message if it is a weekday or weekend. The key for each item is a number (as a string) from 0-6 and corresponds to a numbering system used in the datetime module to refer to the days of the week, where 0 = Sunday, 1 = Monday etc. The values are lists comprised of two items, the text of the day name and the corresponding message. This makes it easier to change the code if I wanted it to print the day instead of the message. 
    References:
        https://www.w3schools.com/python/python_datetime.asp - the Datetime module, which contains the functions .now() and .strftime() which were both used in the code.

Week 6 squareroot.py
    Explanation of code:
        I decided to use Newton's Method to approximate the square root, as suggested. I watched the video in the references below to understand how the method works and based my code off that.

        Newton's Method requires an initial guess to get the ball rolling, so for the function I made, I had that guess be a mandatory argument that the user had to input. I also had a user inputted argument that acted as a limit to how accurate the result would be. A while loop checks how accurate the current guess is by squaring it and finding the difference between it and the number we are trying to find the square root of. If the difference is less than the limit that the user inputted, the function returned the guess. Otherwise, the guess is passed through Newton's Method and a new guess is approximated. This continues until the difference calculted by the while loop is less than the limit. 
    References:
        https://www.youtube.com/watch?v=FMCOebUGG94 - video on Newton's Method by BriTheMathGuy on YouTube

Week 7 numberofEs.py
    Explanation of code:
        In this code, I decided to count all of the "e"s that appear within the text file, regardless of if they were upper or lower case. To do this, I converted all of the letters to lowercase, using the .lower() function. A further expansion of the code could give the number of upper case and number of lower case in the results. 

        I used a try/except as covered in the lab to deal with the case in which the file does not exist, or the file name is incorrect. If this is the case, the program skips the code until the "except" where it prints an error message informing the user of the issue. Otherwise, the code gets executed as normal and the except gets ignored.
        
        The text file is opened using the 'with open()' statements. The file does not need to be appended to or written to, so the file is openend in read only mode. It is also a text file, and we only wish to parse the text within it, so it is opened in text mode. 
        
        A for loop is used to iterate through the lines in the file, and a nested for loop is used to iterate through the letters on each line. An if statement checks if the letter is "e", if true, a counter is incremented by 1. A function called doAddOne() was written to do this inrementation. The results are printed using the print() function.
        
    References:
        The 7.1 Lecture video (around the 10.30 mark) showed how to use a for loop to iterate through a text file. I decided to test to see if a nested loop could access the letters within the line and it worked. 
        https://www.programiz.com/python-programming/methods/string/lower - the .lower() function.

Week 8 plottask.py
    Explanation of code:

    References:
        [numpy.linspace]
        [fonts]
        [label padding]
        [label rotation]
        [setting height and width of figure]
        [turning minor ticks on]
        [major and minor tick editing]