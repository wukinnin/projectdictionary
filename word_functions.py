# import word_dict from word_data.py
from word_data import word_dict

# 1 - add_word
def add_word(word, meaning, details):
    word_dict[word] = {
        "meaning": meaning,
        #details
    }
    print(f"Word '{word}' is added to dictionary.")

# 2 - delete_word
def delete_word(word):
    # Check if word exists in word_dict
    if word in word_dict:
        del word_dict[word]
        print(f"Word '{word}' is deleted from dictionary")
    # If word is not found
    else:
        print(f"Word '{word}' not present in dictionary.")

# 3 - edit_word
def edit_word(word):
    # to be made later
    print()

# 4 - display_word()
def display_words():
    # by default: ascending
    sorted_words = sorted(word_dict.keys()) 

    # loop statement
    for word in sorted_words:
        details = word_dict[word]
        print(f"\n{word}")
        print(f"  Meaning: {details['meaning']}")
        # tbd

# 5 - search_word()
def search_word(word):
    # Check if the word exists in word_dict
    if word in word_dict:
        details = word_dict[word]
        print(f"\nWord: {word}")
        print(f"  Meaning: {details['meaning']}")
        #tbd
    else:
         # If the word is not found
        print(f"Word '{word}' not present in dictionary.")