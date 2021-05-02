"""
Dog years
Write a program which asks a user to input an age in human years, and converts it to the equivalent age in dog years.

Dogs are man's best friend, but they have different lifespans than humans. If you divide the average human
lifespan by the average lifespan of a dog, you can calculate the multiplier for converting an age in human years
to an age in dog years. The average lifespan of a human is 79 years and the average lifespan of a dog is 11 years.

So, 1 human year is equal to 79/11 = 7.18 dog years.

To convert, say, 3 human years to dog years, you'd multiply 3 * 7.18 = 21.54 dog years.

That means, if your dog is 3 years old in human years, they're past their teenage years in dog years!

Here's a sample run of the program (user input is in bold italics):

$ python dog_years.py
Enter an age in human years: 10
That's 71.8 in dog years!
"""

DOG_YEARS = 7.18

def main():
    # Prompt user for input
    print("See how old you are in dog years")
    human_years = float(input("Enter an age in human years: "))

    # Equation to work out dog years
    age_conversion = human_years * DOG_YEARS

    # Return the results to the user
    print("That's " + str(age_conversion) + " in dog years!")


if __name__ == "__main__":
    main()
