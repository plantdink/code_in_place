"""
Write a program which asks the user what their favorite animal is,
and then always responds with "My favorite animal is also ___!"
(the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics):

$ python agreement_bot.py
What's your favorite animal? cow
My favorite animal is also cow!
"""

def main():
    animal = input("What is your favourite animal? ")
    print("My favourite animal is also " + animal + "!")

if __name__ == '__main__':
    main()