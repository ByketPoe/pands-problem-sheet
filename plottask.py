# plottask.py
# The purpose of this program is to plot three different mathematical functions on a graph.
# author: Emma Farrell

# The libraries numpy and matplotlib.pyplot are imported using the import function.
# They are assigned the aliases np and plt respectively to make them easier to call.
# numpy will be used to generate the numbers used in the functions to be plotted.
# matplotlib.pyplot will be used to plot the results on the output plot. 
import numpy as np
import matplotlib.pyplot as plt

# I tried using np.array() to generate numbers for the function, it gave results that aren't granular enough. 
# The step argument for np.array() must be an integer, therefore cannot break down the numbers any further.
# The functions came out as serieses of connected lines with different, gradually increasing slopes. 
# The square and cubic functions were not coming out as curves as they should be. 
# numpy.linspace() returns a series of 50 (by default) evenly spaced float numbers within a specified range.
# This is more suitable for the needs of the plot and allows the functions to be plotted smoothly.
xpoints = np.linspace(0, 4)

# The functions f(x), g(x) and h(x) are calculated as specified in the problem and assigned to variables. 
fofx = xpoints
gofx = xpoints**2
hofx = xpoints**3

# The three functions are plotted using the .plot() function from the matplotlib.pyplot library. 
# These three functions will all appear on the same plot.
# Each function is given a label, which will appear in the legend when the .legend() function is called. 
plt.plot(xpoints, fofx, label = 'Linear Function')
plt.plot(xpoints, gofx, label = 'Square Function')
plt.plot(xpoints, hofx, label = 'Cubic Function')

# Two fonts are defined within dictionaries and set to variables. 
# This sets the font family which will be used, the colour of the text and the size of the text.
font1 = {'family':'serif','color':'darkblue','size': 20}
font2 = {'family':'serif','color':'darkblue','size': 14}

# The plot title and axis labels are created using the .title(), .xlabel() and .ylabel() functions.
# The title/label text is passed as a string to the first argument of the functions.
# The title will appear above the plot, and the axis labels will appear next to their relevant axes.
# fontdict sets the font that will be used by the title/label. In this case, we are using the two fonts defined above. 
# pad and labelpad set the size of 'padding' or space around the title/labels.
plt.title('Varieties of Line Functions', pad = 35, fontdict = font1)
plt.xlabel('Function Input (x)', labelpad = 20, fontdict = font2)
# ylabel by default is rotated 90 degrees. I think this makes it difficult to read, so the rotation is set to 0 like the x label.
# This takes up more space on the plot, but is easier to read.
plt.ylabel('Function Output (f(x))', rotation = 0, labelpad = 70, fontdict = font2)

# The .figure().set_height() and .figure().set_width() functions are used to set the height and width of the window that the plot appears in.
# The default settings meant that the axis labels and title were not visible, especially because I added padding and rotated the y label.
# num = 1 means that these settings will be applied to the plot that is Figure 1.
# In our case, there is only one plot, but this is necessary as otherwise this will create a new empty plot with these settings and not apply these settings to the plot we want.
# The unit of measurement is in inches, so 10 is 10 inches. This setup fits well on my laptop screen, but might be difficult to view on a smallers screen. 
plt.figure(num = 1).set_figheight(10)
plt.figure(num = 1).set_figwidth(20)

# This function ensures that the legend appears on the plot. It uses the label information provided in the .plot() function.
# By setting shadow = True, a shadow appears below the legend box which helps it to stand out. 
plt.legend(shadow = True)

# By default, no gridlines appear on the plot.
# I think they are useful, so I have major and minor gridlines appear on the plot.
# Using the .grid() function, major gridlines appear on the plot, but no minor gridlines.
# The .minorticks_on() function is required to have them appear on the plot.
plt.minorticks_on()
# Using .grid(), the settings of the gridlines can be defined.
# 'which' allows me to specify which kind of gridline I want to change, allowing me to give them separate characteristics.
# 'lw' allows me to specify line weight. I made the major gridlines thicker than the minor gridlines. 
# 'color' allows me to specify colour. I set both to be black to make the plot uniform and make sure the gridlines were not distracting. 
# 'alpha' allows me to set how visible the line is on a scale from 0 to 1. The minor gridlines are more faded than the major gridlines. 
plt.grid(which = 'major', lw = 1.5, color = 'black', alpha = 0.4)
plt.grid(which = 'minor', lw = 1.0, color = 'black', alpha = 0.1)

# The plt.show() function allows the plot to appear on screen according to all of the specifications given in the code previously. 
plt.show()