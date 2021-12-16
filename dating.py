#!/usr/bin/env python3

# Created by: Melody berhane
# Created on: Dec 2021
# This program uses a compound boolean statement to see if the user
# can date the grandchild

def main():

    # Get input from user
    user_wealth_input = input("Are you rich?(y/n): ")
    user_looks_input = input("Are you handsome?(y/n): ")
    print("")

    # Check if the user is good enough to date the grandchild
    if user_wealth_input == "Y" or user_wealth_input == "y"\
       or user_looks_input == "Y" or user_looks_input == "y":
        print("You can date our grandchild!")
        print("\033[1;35;38mThanks for playing")
    elif user_wealth_input == "N" or user_wealth_input == "n"\
            and user_looks_input == "N" or user_looks_input == "n":
        print("Please look for someone else to date.")
        print("\033[1;35;38mThanks for playing")
    else:
        print("Please enter either y/n.")
        print("\033[1;35;38mThanks for playing")


if __name__ == "__main__":
    main()
