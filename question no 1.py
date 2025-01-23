def tester(givenstring="Too short"):
    """
    This function checks the length of the input string.
    If the string is less than 10 characters, it uses the default value.
    Otherwise, it prints the provided string.
    """
    if len(givenstring) < 10:
        print("Too short")
    else:
        print(givenstring)

def main():
    """
    Main function that prompts the user for input and calls the tester function.
    If the user inputs 'quit', the program terminates.
    """
    while True:
        user_input = input("Write something (quit ends): ")
        if user_input.lower() == "quit":
            break
        tester(user_input)

# Run the main function
if __name__ == "__main__":
    main()
