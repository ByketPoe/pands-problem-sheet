# bmi.py
# The purpose of this program is to calculate bmi based on user inputs of height and weight
# author: Emma Farrell

# Request input from user for weight, cast as a float and assign to variable height
weight = float(input('Please enter your weight (in kilograms): '))

# Request input from user for height, cast as a float and assign to variable height
# Need to divide by 100 as input is in centimetres and calculation requires metres
height = (float(input('Please enter your height (in centimetres): ')))/100

# calculate BMI and assign result to variable bmi
bmi = round(weight/(height**2), 2)

# Print result
print(bmi)