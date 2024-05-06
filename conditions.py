# input two numbers from user and determin the greater of the two
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{y} is less than {x}")
else:
    print(f"{x} is equal to {y}")

# Thanks for looking
