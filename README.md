# pands-problem-sheet
Submission for PandS problem sheets

Week 2 bmi.py 
    This program works by taking in height and weight measurements from the user and using them to calculate bmi. The input and print functions and casting data to desired data type (in this case, float) have been covered in lecture material. The round function was found on W3 schools at the link in the reference. This function works by taking in the number to be rounded as well as the number of decimal places that is required: 
        round(<number>, <number of decimal places>). 
    These calculations work by assigning the values inputted and calculated to variables, which has been covered in lecture material. 
    The formula for BMI is weight divided by height squared, and is taken from the link in the references.
    References:
        Round function:     https://www.w3schools.com/python/ref_func_round.asp
        BMI formula:        https://www.wolframalpha.com/input/?i=bmi
        

Week 3 secondstring.py
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

Week 5 weekday.py