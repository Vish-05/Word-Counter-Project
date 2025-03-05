"""Function that counts the number of words in the given text."""
def count_words(text):
    if not text.strip():  # Check if input is empty or just spaces
        return 0   # Will return 0 as no words found
    else:
        words = text.split()  # Split text by whitespace
        return len(words) # Will return the count by finding length of the list saved

"""Main codes to execute the word counter program."""
print("\nWelcome to the Word Counter Program!") 
a = input("Enter a sentence or paragraph: ") # Getting user input
word_count = count_words(a) 
print('Word Count :',word_count) 