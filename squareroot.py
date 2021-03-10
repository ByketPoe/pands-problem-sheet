# squareroot.py
# The purpose of this program is to 
# author: Emma Farrell

# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

# You should create a function called <tt>sqrt</tt> that does this.

# I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

# This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).

# I suggest that you look at the newton method at estimating square roots.

# This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

def sqrt(n, i, r):

    x1 = i 
    xn = x1
    #roundedxn = 0.0

    while abs(xn**2 - n) > 0.0001:
        print("values are: ", round(xn**2, r), round(n, r))
        print("difference is: ", abs(xn**2 - n))
        fx = xn**2 - n
        fdx = 2*xn
        xnplus1 = xn - (fx/fdx)
        xn = xnplus1
        #roundedxn = round(xn, r)
        #print("roundedxn is: ", roundedxn)
        print("xn is: ", xn)
        print("difference2 is: ", abs(xn**2 - n))
    
    return xn

print(sqrt(7.0, 3, 2))