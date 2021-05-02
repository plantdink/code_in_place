"""
Remainder division
Ask the user for two numbers, one at a time, and then print the result of dividing
the first number by the second and also the remainder of the division.

Here's a sample run of the program (user input is in bold italics):

$ python remainder.py
Please enter an integer to be divided: 5
Please enter an integer to divide by: 3
The result of this division is 1 with a remainder of 2
"""

def main():
    # Prompt the user to input number to be divided
    num1 = int(input("Please enter an integer to be divided: "))

    # Prompt the user to input number to divide by
    num2 = int(input("Please enter an integer to divide with: "))

    # Equation
    quotient = num1 // num2
    remainder =  num1 % num2

    # return the results to the user
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == "__main__":
    main()