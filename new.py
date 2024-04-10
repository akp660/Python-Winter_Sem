# Function to sort words alphabetically
def sort_words(words):
    word_list = words.split(", ")  # Split the input string into a list of words
    sorted_words = sorted(word_list)  # Sort the list of words alphabetically
    return sorted_words

# Main program
def main():
    # Input comma-separated words
    input_words = input("Enter comma-separated words: ")
    
    # Sort words alphabetically
    sorted_words = sort_words(input_words)
    
    # Print sorted words
    print("Sorted words: ", ", ".join(sorted_words))

if __name__ == "__main__":
    main()
