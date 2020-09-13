def print_hello():
    """ This is a comment that describes the function. """
    print("Hello!")

def print_goodbye():
    print("Bye!")

def main():
    """ This is my main program function """
    print_hello()
    print_goodbye()

# Only run the main function if we are running this file. Don't run it
# if we are importing this file.
if __name__ == "__main__":
    main()