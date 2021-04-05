# pands-problem-sheet
## Emma Farrell's Submission for PandS problem sheets

### Week 2 bmi.py 
The purpose of this program is to calculate bmi based on user inputs of height and weight
#### Explanation of code:
This program works by taking in height and weight measurements from the user and using them to calculate bmi. The input and print functions and casting data to desired data type (in this case, float) have been covered in lecture material. The round function was found on W3 schools at the link in the reference. This function works by taking in the number to be rounded as well as the number of decimal places that is required: 
            
            round(<number>, <number of decimal places>). 

These calculations work by assigning the values inputted and calculated to variables, which has been covered in lecture material. 
The formula for BMI is weight divided by height squared, and is taken from the link in the references.
#### References:
Round function - https://www.w3schools.com/python/ref_func_round.asp

BMI formula - https://www.wolframalpha.com/input/?i=bmi
        

### Week 3 secondstring.py
The purpose of this program is to take in text and return every second letter in reverse order.
#### Explanation of code:
Strings are an example of something that is iterable i.e. a sequence of data. Iterable data types use numbers called indexes to refer to the position of the data within the sequence, starting at 0. When referring to indexes in reverse, the index starts at -1. 
        
This program uses string slicing to return every second character of a string in reverse. String slicing uses the indexes of a string to determine what characters to remove and which to keep, and were found at the links below. 
String slicing works in the following way, where stringVariable contains a string:
            
            stringVariable[<start>:<stop>:<step>]
        
An iterable (in this case, a string) followed by square brackets means that the indexes of the iterable are being used to refer to the contents. Slicing uses the indexes to determine where to start, stop and step through. So for example someString[3:8:2] would return every second character from the string from index 3 up to (but not including) index 8. A minus number reverses the direction of the indexes. 
        
In this program, string slicing is used to return every second character in a string in reverse order.
#### References:
Slicing Strings links:
- https://www.w3schools.com/python/python_strings_slicing.asp
- https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3


### Week 4 collatz.py
The purpose of this program is to take a value from a user and output the values of a series of calculations performed on that number.
#### Explanation of code:
The sample output in the question shows the numbers as integers, so the input number is cast as an integer and integer division (//) is used in the calculation. A while loop checks the current value of the input initially and after each time the calculations are done. The while loop terminates once the value reaches 1. 
        
Within the while loop, an if statement checks if the value is even or odd. The remainder (modulus [%]) of the input value when divided by 2 is calculated to determine if it is odd or even. If it is even, the remainder will be 0, otherwise it is odd. The if statment executes the calculation to divide the value by 2 if it is even; otherwise the else statement executes the multiplication by 3 and addition of 1 to the value. Because there are only two possible outcomes from the if statement (the value is odd or even) there is no need to check again using an elif statement. 
        
By adding 1 to the odd value, the value will always eventually reduce down to 1 by being divided by 2 on the next iteration as it will be even. This ensures the while loop does not execute infinitely. 
        
The sample output given in the question showed the calculated values in a row on one line. I decided the best way to replicate this would be to create a list to hold all of the values in. The initial value entered is added to the list when it is initially created. 

            resultList = [inputInt]

After the calculations are done on the value, the new value is also added to the list at the end of every iteration of the loop. 

            resultList.append(inputInt)

This list is then printed at the end to show the results.

#### References:
- Lists - https://www.w3schools.com/python/python_lists.asp 
- Appending to lists - https://www.w3schools.com/python/python_lists_add.asp 
- Modulus - https://realpython.com/python-modulo-operator/

### Week 5 weekday.py
The purpose of this program is to return a message corresponding the day of the week it is today.
#### Explanation of code:
The datetime module is used for two functions in the code; the function to obtain the current date and the function to convert it to show the day of the week. 

            now = datetime.datetime.now()
            day = now.strftime("%w")

The code uses a dictionary to store the days of the week and a link to a corresponding output message to display if it is a weekday or weekend. The key for each item is a number (as a string) from 0-6 and corresponds to a numbering system used in the datetime module to refer to the days of the week, where 0 = Sunday, 1 = Monday etc. The values are lists comprised of two items, the text of the day name and a the vairable that contains the corresponding message. This makes it easier to change the code if I wanted it to print the day instead of the message. 

            daysOfWeek = {"0": ["Sunday", weekendMsg], 
                            "1": ["Monday", weekdayMsg], 
                            "2": ["Tuesday", weekdayMsg], 
                            "3": ["Wednesday", weekdayMsg], 
                            "4": ["Thursday", weekdayMsg], 
                            "5": ["Friday", weekdayMsg], 
                            "6": ["Saturday", weekendMsg]}

The messages used to show if it a weekday or weekend are saved to variables and are called from the dictionary items. This saves me from having to write the messages multiple times. 

            weekendMsg = "It is the weekend, yay!"
            weekdayMsg = "Yes, unfortunately today is a weekday"

#### References:
Datetime module - https://www.w3schools.com/python/python_datetime.asp - this contains the functions .now() and .strftime() which were both used in the code.

### Week 6 squareroot.py
The purpose of this program is to find an approximation of the square root of a number. 
### Explanation of code:
I decided to use Newton's Method to approximate the square root, as suggested. I watched the video in the references below to understand how the method works and based my code off that.

Newton's Method requires an initial guess to get the ball rolling, so for the function I made, I had that guess be a mandatory argument that the user had to input. 
            
            def sqrt(num, initGuess, resolution): 
                xn = initGuess 

I also have a user inputted argument that acted as a limit to how accurate the result would be (resolution). 

A while loop checks how accurate the current guess is by squaring it and finding the difference between it and the number we are trying to find the square root of. If the difference is less than the limit that the user inputted, the function returned the guess. Otherwise, the guess is passed through Newton's Method and a new guess is approximated. This continues until the difference calculted by the while loop is less than the limit: 
            
            while abs(xn**2 - num) > resolution:
                <code to be executed in loop>

The rest of the function follows Newton's method according to the video in the reference. The user is asked for the number they want to find the square root of, the initial guess and an 'accuracy limit' so they can decide how close of an answer they want. The result is printed to the user. 

#### References:
Video on Newton's Method by BriTheMathGuy on YouTube - https://www.youtube.com/watch?v=FMCOebUGG94

### Week 7 es.py
The purpose of this program is to count the number of times the letter "e" appears in a text file.
#### Explanation of code:
In this code, I decided to count all of the "e"s that appear within the text file, regardless of if they were upper or lower case. To do this, I converted all of the letters to lowercase, using the .lower() function. A further expansion of the code could give the number of upper case and number of lower case in the results. 

            lowletter = letter.lower()

I used a try/except as covered in the lab to deal with the case in which the file does not exist, or the file name is incorrect. If this is the case, the program skips the code until the "except" where it prints an error message informing the user of the issue. Otherwise, the code gets executed as normal and the except gets ignored.
        
The text file is opened using the 'with open()' statements. The file does not need to be appended to or written to, so the file is openend in read only mode. It is also a text file, and we only wish to parse the text within it, so it is opened in text mode. 

            with open(fileToParse, "rt") as f:
        
A for loop is used to iterate through the lines in the file, and a nested for loop is used to iterate through the letters on each line. 

            for line in f:
                for letter in line:
                    <code to be executed in loop>

An if statement checks if the letter is "e", if true, a counter is incremented by 1. A function called doAddOne() was written by me to do this inrementation. The results are printed using the print() function.
            if lowletter == 'e':
                count = doAddOne(count)
        
#### References:
The 7.1 Lecture video (around the 10.30 mark) showed how to use a for loop to iterate through a text file. I decided to test to see if a nested loop could access the letters within the line and it worked. 

The .lower() function - https://www.programiz.com/python-programming/methods/string/lower

### Week 8 plottask.py
The purpose of this program is to plot three different mathematical functions on a graph.
#### Explanation of code:
The libraries numpy and matplotlib.pyplot are used. numpy is used to generate data to be used in the plot, matplotlib.pyplot is used to create the plot. I intially tried to use numpy.array() to generate the data as shown in the lab, but the plots that were created did not look right. The lines produced on the plot were angular when they should be curved (i.e. for the squared and cubed functions). I realised the the arrays consisted of 4 integers, so there was not enough data for the plots to generate smooth lines. I found the function numpy.linspace() which returns a series of 50 (by default) evenly spaced float numbers within a specified range. This is more suitable for the needs of the plot and allows the functions to be plotted smoothly. The results of this function are passed to the variable xpoints, as this will be our array of x points used in our function.

The y points are calculated for f(x), g(x) and h(x) and assigned to variables. The points are plotted using the .plot() function, which takes in the x points and the y points. They will all appear on the same plot. The .plot() function also takes in a label argument, which can be used to create a legend, making it easier to know what each line on the plot represents. 

Two dictionaries are created and saved to variables. These will be used to format the text used in the title and axis labels. The plot title and axis labels are created using the .title(), .xlabel() and .ylabel() functions. The title/label text is passed as a string to the first argument of the functions. The title will appear above the plot, and the axis labels will appear next to their relevant axes. 

            plt.title('Varieties of Line Functions', pad = 35, fontdict = font1)
            plt.xlabel('Function Input (x)', labelpad = 20, fontdict = font2)
            plt.ylabel('Function Output (f(x))', rotation = 0, labelpad = 70, fontdict = font2)

The argument fontdict sets the font that will be used by the title/label. In this case, we are using the two font dictionaries defined previously. The arguments pad and labelpad set the size of 'padding' or space around the title/labels. The Y axis label by default is rotated 90 degrees; I think this makes it difficult to read, so the rotation argument is set to 0. This will take up more space on the plot, which is a trade-off I have decided to make for legibility. The rotation is 0 by default for the x axis label and title.

When I generated the plot, I found that a lot of the important information (title, axis labels) was hidden because the window was too small. To change this, I used the .figure() function to set the width and height of the window the plot appeared in when it was generated:

            plt.figure(num = 1).set_figheight(10)
            plt.figure(num = 1).set_figwidth(20)

The argument num = 1 means that these settings will be applied to the plot that is Figure 1. In this case, there is only one plot, but this is necessary as otherwise this will create a new empty plot with these settings and will not apply these settings to the plot we want. The unit of measurement is in inches, so 10 is 10 inches. This setup fits well on my laptop screen, but might be difficult to view on a smallers screen. 

The .legend() function is used to create the legend that will appear on the plot, making it easier to read and identify what each line represents. It uses the label information provided in the .plot() function. By setting shadow = True, a shadow appears below the legend box which helps it to stand out. 

            plt.legend(shadow = True)

By default, no gridlines appear on the plot.I think they are useful, so I have major and minor gridlines appear on the plot. Using the .grid() function, major gridlines appear on the plot, but no minor gridlines. The .minorticks_on() function is required to have them appear on the plot.

            plt.minorticks_on()
            plt.grid(which = 'major', lw = 1.5, color = 'black', alpha = 0.5)
            plt.grid(which = 'minor', lw = 1.0, color = 'black', alpha = 0.1)  

Using the .grid() function, the settings of the gridlines can be defined. The argument 'which' allows me to specify which kind of gridline I want to change, allowing me to give them separate characteristics. The argument 'lw' allows me to specify line weight. I made the major gridlines thicker than the minor gridlines. The argument 'color' allows me to specify colour. I set both to be black to make the plot uniform and make sure the gridlines were not distracting. The argument 'alpha' allows me to set how visible the line is on a scale from 0 to 1. The minor gridlines are more faded than the major gridlines. 

The .show() function create the plot in a new window according to the settings in the code.

#### References:
- The numpy.linspace() function - https://www.geeksforgeeks.org/numpy-linspace-python/
- Fonts - https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html
- Label padding - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html 
- Title Padding - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html 
- Label rotation - https://stackoverflow.com/questions/27671748/how-to-print-y-axis-label-horizontally-in-a-matplotlib-pylab-chart
- Setting height and width of figure - https://stackabuse.com/change-figure-size-in-matplotlib/
- Turning minor ticks on - https://stackoverflow.com/questions/19940518/cannot-get-minor-grid-lines-to-appear-in-matplotlib-figure
- Grid editing - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html