"""
First person Karel
Write a program that lets you play Karel in a rectangular world (moving and turning left and not walking off
of the world, all that good stuff)!

Have you ever wanted to be Karel, wandering about a nice rectangular world, not a worry in the world,
just moving and turning left whenever you'd like? You can emulate this feeling by writing a console-based
first person Karel program! For simplicity, assume that beepers and painting are out of the question, and the world
has no walls. All you should implement is moving and turning left. Store the number of columns and rows in your
"world" as constants, and assume you start in row 1 column 1 facing East. Prompt the user for an action
("move" or "turn left" until they press enter without typing anything, in which case the result of input() will be
an empty string, and you can stop looping).

Recall that you can only move if you're not about to move off of the world!
This means you can only move in the following cases:
facing East and current column is less than the number of columns (move right)
facing West and current column is greater than 1 (move left)
facing North and current row is less than the number of rows (move up)
facing South and current row is greater than 1 (move down)

Here's what turning left does to the direction you (Karel) are facing:
if you're facing East, turning left will make you face North
if you're facing North, turning left will make you face West
if you're facing West, turning left will make you face South
if you're facing South, turning left will make you face East

Here's a sample run of the program (user input is in bold italics):

$ python karel.py
Welcome to first person Karel. You're at row 1, column 1, facing East (facing column 3)
What would you like to do? You can move and turn left. Press enter to finish. move
You moved one step forward and now you're at row 1 column 2
What would you like to do? You can move and turn left. Press enter to finish. turn left
You turned left and are now facing North.
What would you like to do? You can move and turn left. Press enter to finish. turn left
You turned left and are now facing West.
What would you like to do? You can move and turn left. Press enter to finish. move
You moved one step forward and now you're at row 1 column 1.
What would you like to do? You can move and turn left. Press enter to finish. move
You can't move forward!
What would you like to do? You can move and turn left. Press enter to finish.
You've ended up at row 1 and column 1 facing West.

This may be a confusing problem (it's certainly a pretty big problem)!
If you'd like a hint about how to get started, scroll down and keep reading
(though we recommend you give it your best shot first!).
If you're feeling good, stop reading right here and go right ahead!

As a hint, this is what the beginning of our solution code looks like:

# notice these constants!
N_COLS = 3
N_ROWS = 3

def main():
    print("Welcome to first person Karel. You're at row 1, column 1, facing East (facing column " + str(N_COLS) + ")")
    # this variable will keep track of the way Karel is facing -- it changes if the user says to "turn left"!
    facing_direction = 'East'
    # this variable ...
    curr_col = 1
    # ... and this one keep track of Karel's position in the world! they may change if the user says to "move"
    curr_row = 1
    action = input("What would you like to do? You can move and turn left. Press enter to finish. ")
    # ... more code! there's a while loop that starts on this line, but our hint ends here :^)

"""

WORLD_COLS = 6
WORLD_ROWS = 6