# linear search

import sys
from cs50 import get_string

# Names in a phone book of previos CS50 instructors
book = [
    "Chen",
    "Kernighan",
    "Leitner",
    "Lewis",
    "Malan",
    "Muller",
    "Seltzer",
    "Shieber",
    "Smith"]

# Prompt user for name

name = get_string("Name: ")
if name in book:
    print(f"Calling {name}")
    sys.exit(0)
print("Quitting")

# Thanks for looking
