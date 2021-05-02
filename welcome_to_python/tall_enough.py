"""
Tall enough to ride
Write a program which asks the user how tall they are and prints whether or not they're taller than a
pre-specified minimum height. In amusement parks (ah, the good old pre-pandemic days...), rollercoasters
frequently have minimum height requirements for safety reasons.  Assume for now that the minimum height is
50 of whatever height unit you'd like :)

Here's a sample run (user input is in bold italics):

$ python tall_enough.py
How tall are you? 100
You're tall enough to ride!

(For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or
not they're tall enough to ride, until the user doesn't enter an age at all, in which case the program stops.
Curious about how to do this? See the function tall_enough_extension() in the solution code!)
"""

MIN_HEIGHT = 50

"""
def main():
    # prompt user to enter their height
    height = float(input("How tall are you? "))

    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("Sorry, you're NOT tall enough to ride :(")
"""

# tall_enough_extension
def main():
    height = float(input("How tall are you? "))
    while height != "":
        height = float(height)
        # if the user presses Enter immediately (without typing anything), the result of input() will be an empty string
        # (nothing between the quotation marks)
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("Sorry, you're NOT tall enough to ride :(")
        height = input("How tall are you? ")

if __name__ == "__main__":
    main()