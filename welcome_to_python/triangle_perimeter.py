"""
Perimeter of a triangle
Prompt the user to enter the lengths of each side of a triangle and then calculate and
print the perimeter of the triangle (the sum of all of the side lengths).
Here's a sample run of the program (user input is in bold italics):

$ python perimeter.py
What is the length of side 1? 3
What is the length of side 2? 4
What is the length of side 3? 5.5
The perimeter of the triangle is 12.5
"""

def main():
    # Prompts to user to enter the length of the triangle sides
    side1 = float(input("Please enter the length of the first side of a triangle: "))
    side2 = float(input("Please enter the length of the second side of a triangle: "))
    side3 = float(input("Please enter the length of the third side of a triangle: "))

    # function to calculate the perimeter of the triangle
    perimeter = side1 + side2 + side3

    # return the result to the user
    print("The perimeter of the triangle is " + str(perimeter))

if __name__ == '__main__':
    main()