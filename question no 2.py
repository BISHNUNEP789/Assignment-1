def grocery_list():
    items = []  # Initialize an empty list

    while True:
        print("\nWould you like to")
        print("(1)Add or")
        print("(2)Remove items or")
        print("(3)Quit?: ", end="")
        choice = input().strip()

        if choice == "1":  # Add item
            item = input("What will be added?: ").strip()
            items.append(item)

        elif choice == "2":  # Remove item
            if items:  # Check if the list is not empty
                print(f"There are {len(items)} items in the list.")
                try:
                    index = int(input("Which item is deleted?: ").strip())
                    if 0 <= index < len(items):  # Valid index
                        items.pop(index)
                    else:  # Invalid index
                        print("Incorrect selection.")
                except ValueError:  # Non-integer input
                    print("Incorrect selection.")
            else:
                print("The list is empty, nothing to remove.")

        elif choice == "3":  # Quit
            print("\nThe following items remain in the list:")
            for item in items:
                print(item)
            break

        else:  # Invalid option
            print("Incorrect selection.")

# Call the function to run the program
grocery_list()
