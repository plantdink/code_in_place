"""
Now that you’ve seen how programming can help us in a number of different areas, it’s time for you to implement
Khansole Academy—a program that helps other people learn! In this problem, you’ll write a program in the file
khansole_academy.py that randomly generates a simple addition problem for the user, reads in the answer from the user,
and then checks to see if they got it right or wrong. Note that “console” is another name for “terminal” :-).

More specifically, your program should be able to generate simple addition problems that involve adding two 2-digit
integers (i.e., the numbers 10 through 99). The user should be asked for an answer to the generated problem.
Your program should determine if the answer was correct or not, and give the user an appropriate message to let
them know.

A sample run of the program is shown below (user input is in bold italics).
$ python khansole_academy.py
What is 51 + 79?
Your answer: 120
Incorrect. The expected answer is 130

Here's another sample run, where the user gets the question correct:
$ python khansole_academy.py
What is 55 + 11?
Your answer: 66
Correct!

Prints out a randomly generated addition problem and checks if the user answers correctly.
"""

import random

NUM1 = random.randint(10, 99)
NUM2 = random.randint(10, 99)

def main():
    sum = NUM1 + NUM2
    print("What is", str(NUM1), "+", str(NUM2))
    answer = int(input("Your answer: "))
    if answer == sum:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is", str(sum))

if __name__ == '__main__':
    main()
