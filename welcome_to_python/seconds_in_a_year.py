"""
Seconds in a year
Use Python to calculate the number of seconds in a year, and tell the user what the result is in a
nice print statement! You should use constants for this exercise -- there are 365 days in a year,
24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
"""

DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

def main():
    # Equation to calculate the number of seconds in a year
    seconds_in_year = SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY * DAYS_IN_YEAR

    # Return the result to the user
    print("There are " + str(seconds_in_year) + " seconds in a 365 day year")


if __name__ == "__main__":
    main()