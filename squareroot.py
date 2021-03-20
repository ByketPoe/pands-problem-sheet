# squareroot.py
# The purpose of this program is to find an approximation of the square root of a number. 
# author: Emma Farrell

# The def() statement creates the function, in this case "sqrt()".
# Three arguments must be entered when using the function. 
# These represent the number the user wants to find the square root of, an initial guess, and a resolution. 
def sqrt(num, initGuess, resolution):
    # The initial guess is set to the variable xn. 
    # In Newton's Method, this  number is passed through the function iteratively and approximates the square root with each iteration.
    # The first iteration is x1, the second x2 etc. 
    xn = initGuess 
    # The iterations are controlled using a while loop. 
    # This will continue to interate while xn gets closer to the square root of num.
    # The absolute value of the difference between xn squared and the number we are trying to find the square root of is calculated.
    # In order to prevent the loop from iterating infinitely, we ask for an accuracy limit from the user. 
    # When the difference calculated is below this limit, the loop will stop iterating and the current value of xn will be returned as the square root of num. 
    # The absolute value is used to account for if the guess squared is less than the number we are trying to find the square root of giving a minus number. 
    # This would always be less than the resolution and may cause the loop to terminate early, so abs() returns a positive number.
    while abs(xn**2 - num) > resolution:
        # Below are the steps outlined in Newton's Method. 
        # Since x is the square root of the number, the number = x squared.
        # Moving the number to the other side of the equation gives 0 = x**2 - number. This gives us the root of the equation f(x).
        fx = xn**2 - num
        # Using basic calculus, we find that the derivative of f(x) (known as f'(x)) is 2x.
        fdx = 2*xn
        # The next iteration of x is xn minus f(x) divided by f'(x), according to Newton's Method.
        # This is calculated and assigned to the variable xnplus1
        xnplus1 = xn - (fx/fdx)
        # xn is now made equal to xnplus1, which will be checked by the while loop to see if it is in rage of being the sqaure root of the number.
        # If not, it will loop through Newton's Method again and a new approximation is calculated. 
        xn = xnplus1
    
    # The current value of xn is returned.
    return xn

# The user is asked to input the number that they want to find the square root of, along with a guess and a limit value.
# The inputs are cast as floats. 
sqrNum = float(input("Please enter the number you wish to find the square root of: "))
guess = float(input("Please enter an initial guess for the square root: "))
res = float(input("Please enter an accuracy limit (0.0001 recommended): "))

# The function I created "sqrt" is invoked to find the square root of the input number. 
# The arguments defined when the user entered the numbers are passed into the function.
# The result is printed to the console using the print() function. 
print(sqrt(sqrNum, guess, res))