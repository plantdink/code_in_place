"""
This program simulates rolling two dice, and prints the results of each role as well as the total
"""

import random


# Number of sides on each dice
NUM_SIDES = 6


def main():
    # setting a seed value is useful for debugging
    # random.seed(1)
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("The dice have", NUM_SIDES, "sides_each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()