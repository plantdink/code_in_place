"""
Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end.
"""

def main():
    anton = 21
    beth = 6 + anton
    chen = 20 + beth
    drew = chen + anton
    ethan = chen

    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " +str(drew))
    print("Ethan is " + str(ethan))

if __name__ == '__main__':
    main()