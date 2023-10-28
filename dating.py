#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Oct/28/2023
# This program tells the user if they're eligible to date my grandchild given their age.


def main():
    # Declaring variable to allow the user to input their age.
    user_age_as_string = input("Enter your age: ")

    # Initiating try catch.
    try:
        user_age_as_integer = int(user_age_as_string)
        # Using If statement to see if the user's age is < 0 or > 120.
        if (user_age_as_integer < 0) or (user_age_as_integer > 120):
            print("Invalid age.")
        # Using else if to see if the user's age is < 25.
        elif user_age_as_integer < 25:
            print("You're too young to date my grandchild.")
        # Using else if to see if the user's age is > 40.
        elif user_age_as_integer > 40:
            print("You're too old to date my grandchild.")
        # Using else to tell them they're eligible to date my grandchild.
        else:
            print("You're eligible to date my grandchild.")
    # Catch error statement.
    except ValueError:
        print("{} is not a valid age.".format(user_age_as_string))


if __name__ == "__main__":
    main()
