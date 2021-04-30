"""
Last Monday, NASA made history with the first controlled flight on another planet.
Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity.
On Sunday, Ingenuity made its third flight, during which it flew faster and further than it had on any
of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!
When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due
to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth.
Write a Python program that prompts an Earthling to enter their weight on Earth and prints their
calculated weight on Mars.

Prompts the user for a weight on Earth and prints the equivalent weight on Mars.
"""

MARS_MODIFIER = 37.8


def main():
    print("Find out the weight of something on Mars")
    weight = float(input("Please enter an Earth weight: "))
    mars_weight = (weight / 100) * MARS_MODIFIER
    print("You entered:", weight, "On Mars this is", mars_weight)


if __name__ == "__main__":
    main()