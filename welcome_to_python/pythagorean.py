"""
Pythagorean theorem
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and
outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry.
It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other
two sides.

Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC).
You will probably find math.sqrt() to be useful.

Here's a sample run of the program (user input is in bold italics):

$ python pythagorean.py
Enter the length of AB: 3
Enter the length of AC: 4
The length of BC (the hypotenuse) is: 5.0
"""

import math

def main():
    # Prompt the user to enter values
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    bc = math.sqrt(ab ** 2 + ac ** 2)

    # Return the results to the user
    print("The length of BC (the hypotenuse) is: " + str(bc))


if __name__ == "__main__":
    main()