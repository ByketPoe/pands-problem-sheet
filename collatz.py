# collatz.py
# The purpose of this program is to take a value from a user and output the values of a series of calculations performed on that number.
# If the number is even, it is divided by two, otherwise it is multiplied by 3 and has 1 added to it. 
# This continues until a value of 1 is obtained. 
# author: Emma Farrell

# The initial value is taken from the user and cast as an integer. 
inputInt = int(input("Please enter a positive whole number: "))

# The question mentioned outputting the values, so I decided to create a list to store the values in.
# The list starts with the initial value in it. 
resultList = [inputInt]

# A while loop executes the code continuously until the calculations reduce the input value to 1. 
while inputInt != 1:
    # An if statement checks if the input value is even by using the modulus to calculate the remainder when dividing by 2.
    # If the remainder is zero, that means the value is even. 
    # If true, the value is divided by 2.
    if inputInt % 2 == 0:
        inputInt //= 2 # Integer division is used. This is to maintain the values as integers. 
        # The sample output given in the question shows integers, so I will maintain the values as such.
    else: # The only other possibility is that the value is odd, so no need for an elif statement. 
        # If the value is odd, it is multiplied by 3 and has one added to it. 
        # The value will then become even and this helps ensure the value will eventually reduce to 1, ensuring the loop is not infinite. 
        inputInt *= 3
        inputInt += 1
    # The new value is appended to the list that will be used to output the results.
    resultList.append(inputInt)

# The list is printed to output all of the values obtained, including the initial value. 
print(resultList)