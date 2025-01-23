def my_split(sentence, separator):
    """
    Splits a sentence into a list of items using the given separator.
    """
    result = []
    current_item = ""
    for char in sentence:
        if char == separator:
            result.append(current_item)
            current_item = ""
        else:
            current_item += char
    result.append(current_item)  # Add the last item
    return result

def my_join(items, separator):
    """
    Joins a list of items into a single string separated by the given separator.
    """
    result = ""
    for i, item in enumerate(items):
        result += item
        if i < len(items) - 1:  # Add separator between items but not at the end
            result += separator
    return result

def main():
    # Prompt user for input
    sentence = input("Please enter sentence: ")
    separator = " "  # Use space as the separator for splitting

    # Split the sentence
    split_result = my_split(sentence, separator)

    # Join the split items with a comma
    joined_result = my_join(split_result, ",")

    # Print the results
    print(joined_result)
    for item in split_result:
        print(item)

if __name__ == "__main__":
    main()
