"""
Ask the user for a number and print its square (the product of the number times itself).
Here's a sample run of the program (user input is in bold italics):

$ python square.py
Type a number to see its square: 4
4.0 squared is 16.0
"""

def main():
    # cast the number to a float so that maths can be done with it
    number = float(input("Type a number to see its square: "))
    # number * number is equivalent to number**2
    print(str(number) + " squared is " + str(number**2))

if __name__ == '__main__':
    main()