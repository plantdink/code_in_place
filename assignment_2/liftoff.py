"""
Write a program in the file liftoff.py that prints out the calls for a spaceship that is about to launch.
Countdown from 10 to 1 and then output Liftoff! Your program should use a for loop.
Here's a sample run of the program:

$ python liftoff.py
10
9
8
7
6
5
4
3
2
1
Liftoff!

Prints out a spaceship launch sequence.
"""


def main():
    for i in range(10, 0, -1):
        print(i)
    print("Liftoff!")


if __name__ == '__main__':
    main()
