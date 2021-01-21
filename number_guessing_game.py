#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if u got the right random number
def main():
    import random
    # this program checks if the random numbers match
    # input
    random_number = random.randint(1, 8)
    # process
    try:
        while True:
            positive_integer_as_string = input("enter a number from 1, 8:")
            positive_integer = int(positive_integer_as_string)
            if positive_integer == random_number:
                print("Correct")
                break
            else:
                print("Try again ")
    except Exception:
        print("Not the right number")


if __name__ == "__main__":
    main()
