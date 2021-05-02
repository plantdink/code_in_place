"""
Fahrenheit to Celsius

Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!)
and outputs the temperature converted to Celsius.
The Celsius scale is widely used to measure temperature, but places like the US still use Fahrenheit.
Fahrenheit is another unit for temperature, but the scale is different from Celsius --
for example, 0 degrees Celsius is 32 degrees Fahrenheit!

The equation you should use for converting from Fahrenheit to Celsius is the following:

degrees_celsius = (degrees_fahrenheit - 32) * 5/9

Here's a sample run of the program (user input is in bold italics):

$ python f_to_c.py
Enter temperature in Fahrenheit: 76
Temperature: 76.0F = 24.444444444444443C
"""

def main():
    # User prompt to enter temperature to convert
    degrees_fahrenheit = float(input("Please enter temperature in Fahrenheit: "))

    # Use the formula to calculate the temperature in celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    # return result to user with correct units
    print("Temperature: " + str(degrees_fahrenheit) + "F  = " + str(degrees_celsius) + "C")

if __name__ == "__main__":
    main()



