a = 4
b = 5
c = 6

if a == b:
    print("a is equal to b")

if a != b:
    print("a is not equal to b")

# and
if a < b and a < c:
    print("a is less than b and c")

# Non-exclusive or
if a < b or a < c:
    print("a is less than either b or c (or both)")

# Boolean
a = True
if a:
    print("a is True")

# Not operator
a = False
if not a:
    print("a is False")

# and again
a = True
b = False
if a and b:
    print("a and b are both True")

# Assign the result of a boolean operation to a variable
a = 3
b = 3
c = a == b
# Print c, which should be True
print("c is {}".format(c))

# Zero is False and non-zero is true
# The following will not print anything
if 0:
    print("Zero")

# The following will print
if 'A':
    print("A is non-zero")

# Input function
# temperature = input("What is the temp in Fahrenheit? ")
# print("You said the temp was {}.".format(temperature))

# Convert input to integer or float and compare
# use int to convert to integer and float to convert to float
# if using int and user inputs a decimal, you get a ValueError
temperature = float(input("What is the temp in Fahrenheit? "))
if temperature > 120:
    print("You said the temp was {}.".format(temperature))
    print("You can fry an egg outside.")
elif temperature > 90:
    print("It is hot out.")
elif temperature < 30:
    print("It is cold out.")
else:
    print("It is not hot out.")

# Text comparisons, make case-insensitive
user_name = input("What is your name? ")
if user_name.lower == "son":
    print("Nice name")
else:
    print("OK name")

print("Done")