"""
E = mc^2
Write a program that continually reads in mass from the user and then outputs the equivalent energy
using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass,
and C is the speed of light:

E\ =\ m\cdot C^2
E = m⋅C
2

Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are
related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for
the speed of light -- C = 299792458 m/s.

Here's a sample run of the program (user input is in bold italics):

$ python emc2.py
Enter kilos of mass: 100
e = m * C^2...
m = 100.0 kg
C = 299792458 m/s
8.987551787368176e+18 joules of energy!
"""

# m/s
C = 299792458


def main():
    # Prompt user to input a mass value in kg
    mass_in_kg = float(input("Enter kilograms of mass: "))

    # Calculate energy equivalently energy = mass * (C ** 2) using the ** operator to raise C to the power of 2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Return the result to the user, display the formula
    print("e = m*C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

if __name__ == "__main__":
    main()
