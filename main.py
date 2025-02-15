def main():
    # Set the path to the book file
    book_path = "books/frankenstein.txt"
    
    # Read the book text from the file
    text = get_book_text(book_path)
    
    # Calculate the number of words in the text
    num_words = get_num_words(text)
    
    # Get a dictionary of character counts (all characters, converted to lowercase)
    chars_dict = get_chars_dict(text)
    
    # Convert the dictionary to a sorted list of dictionaries (sorted by count in descending order)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # Print the report header
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    # Iterate over the sorted list and print counts for alphabetic characters only
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    # Print the report footer
    print("--- End report ---")


def get_num_words(text):
    """
    Splits the text into words and returns the total count.
    """
    words = text.split()
    return len(words)


def sort_on(d):
    """
    Helper function for sorting; returns the 'num' value from a dictionary.
    """
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    """
    Converts a dictionary of character counts into a list of dictionaries,
    then sorts the list in descending order based on the count.
    """
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    """
    Iterates over each character in the text, converts it to lowercase,
    and returns a dictionary with character counts.
    """
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    """
    Opens the file at the given path and returns its full text content.
    """
    with open(path) as f:
        return f.read()


# Execute the main function to generate the report
main()
