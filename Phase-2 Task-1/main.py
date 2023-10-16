# Program to read a text file and find all unique words and the occurrences of words
# Written by Shubham Anand Jaiswal
# Terminal run command: python main.py sample.txt

# Import argv to receive file name from user
from sys import argv

# Main function code
def main():
    # Ensure correct number of command line arguments
    if len(argv) != 2:
        print("Usage: python main.py file_name.txt")
        return 1
    
    # Call the function to find unique words
    find_unique_words()
    
    # Exit with code 0 to denote success
    return 0

# Function to find unique words and display the result
def find_unique_words():
    
    # Try opening the file with user entered file name
    try:
        with open(argv[1], "r") as file:
            # Read the file data
            data = file.read()
          
    # If file does not exist, tell the user
    except FileNotFoundError:
        print(f"File {argv[1]} doesn't exist!")
        return 1
    
    # Continue if file correctly opens
    else:   
        # Separate the words in a list
        words = data.strip().split()
        
        # Empty dictionary to store words and their counts
        word_map = {}
        
        # Add the word and their occurences as key-value pairs
        for word in words:
            word = word.strip(".")
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1
        
        # Create list for words whose count is 1 in word_map
        unique_words = [word for (word, count) in word_map.items() if word_map[word] == 1]
        
        # Display the result
        print(f"\nUnique words: \n{unique_words}")
        print(f"\nTotal number of unique words: {len(unique_words)}")
        print(f"\nOccurences of words:\n {word_map}")

# Call main function      
main()
    