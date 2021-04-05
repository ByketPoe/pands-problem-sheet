# plottask.py
# The purpose of this program is to plot three different mathematical functions on a graph.
# author: Emma Farrell

# The libraries numpy and matplotlib.pyplot are imported using the import function.
# They are assigned the aliases np and plt respectively to make them easier to call.
import numpy as np
import matplotlib.pyplot as plt

# Tried np.array, it gave results that aren't granular enough. The step argument must be an integer, therefore cannot break down any further.
# The functions came out as serieses of connected lines with different, gradually increasing slopes. 
# The square and cubic functions were not coming out as curves as they should be. 
# numpy.linspace() returns a series of 50 (by default) evenly spaced float numbers within a specified range.
# This is more suitable for the needs of the plot and allows the functions to be plotted smoothly.
xpoints = np.linspace(0, 4)

# The functions f(x), g(x) and h(x) are calculated as specified in the problem. 
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
font1 = {'family':'serif','color':'darkblue','size': 18}
font2 = {'family':'serif','color':'darkblue','size': 12}

# The plot title and axis labels are created using the .title(), .xlabel() and .ylabel() functions.
# The title/label text is passed as a string to the first argument of the functions.
# The title will appear above the plot, and the axis labels will appear next to their relevant axis.
# fontdict sets the font that will be used by the title/label. In this case, we are using the two fonts defined above. 
# pad and labelpad set the size of 'padding' or space around the title/labels.
plt.title('Varieties of Line Functions', pad = 35, fontdict = font1)
plt.xlabel('Function Input (x)', labelpad = 20, fontdict = font2)
plt.ylabel('Function Output (f(x))', rotation = 0, labelpad = 70, fontdict = font2)

# plt.figure(num = 1, figsize=(20,10), ) #dpi = 80
plt.figure(num = 1).set_figheight(10) #dpi = 80
plt.figure(num = 1).set_figwidth(20) #dpi = 80

plt.legend()

plt.minorticks_on()
plt.grid(which = 'major', lw = 1.5, color = 'black', alpha = 0.5)
plt.grid(which = 'minor', lw = 1.0, color = 'black', alpha = 0.1)
plt.show()