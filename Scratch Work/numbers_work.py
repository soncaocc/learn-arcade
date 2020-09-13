

def print_number(my_number):
    print(my_number)

print_number(55)
print_number(25)
print_number(8)

def add_numbers(a, b):
    print(a + b)

add_numbers(11, 7)

def sum_two_numbers(a, b):
    result = a + b
    return result

# Capture the function's result into a variable
# by puttin g"my_result =" in front of it.
# (Use whatever variable name best describes the data,
# don't blindly use 'my_result' for everything.)

my_result = sum_two_numbers(22, 15) # <=== This line CAPTURES the return value

# Now that I captured the result, print it.
print(my_result) # <=== This is printing, NOT capturing


def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume

six_pack_volume = volume_cylinder(2.5, 5) * 6
print(six_pack_volume)

# This function will print the result
def sum_print(a, b):
    result = a + b
    print(result)

# This function will return the result
def sum_return(a, b):
    result = a + b
    return result

# This code prints the sum of 4+4 because the function has a print
sum_print(4, 4)

# This code prints nothing because the function returns, and doesn't print
sum_return(4, 4)

# This code will not set x1 to the sum.
# The sum_print function does not have a return statement, so it returns
# nothing!
# x1 actually gets a value of 'None' because nothing was returned
x1 = sum_print(4, 4)
print("x1 =", x1)

# This will set x2 to the sum and print it properly
x2 = sum_return(4, 4)
print("x2 =", x2)

def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result


# Pretend you have some code here
x = 45
y = 56

# Wait, how do I print the result of this?
print(calculate_average(x, y))

# x=44
# def f():
#     x += 1
#     print(x)
# f()

def a(x):
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)

def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)

def c(x):
    print("C start and end, x =", x)

a(5)

def a(x):
    x = x + 1
    return x

x = 3
x = a(x)

print(x)

def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)

x = 10
y = 20
a(y, x)

def a(x, y):
    x = x + 1
    y = y + 1
    return x, y

x = 10
y = 20
x2, y2 = a(x, y) # Most computer languages don't support this
print(x2)
print(y2)

def a(my_data):
    print("function a, my_data = ", my_data)
    my_data = 20
    print("function a, my_data = ", my_data)

my_data = 10

print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)

def a(my_list):
    print("function a, list = ", my_list)
    my_list = [10, 20, 30]
    print("function a, list = ", my_list)

my_list = [5, 2, 4]
print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)

def a(my_list):
    print("function a, list = ", my_list)
    my_list[0] = 1000
    print("function a, list = ", my_list)

my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)
