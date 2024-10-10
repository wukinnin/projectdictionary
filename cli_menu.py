# Import the necessary functions from word_functions.py
from word_functions import add_word, delete_word, edit_word, display_words, search_word

# Define the CLI menu
def cli_menu():
    while True:
        print("\n--- Word Dictionary Menu ---")
        print("1. Add Word")
        print("2. Delete Word")
        print("3. Edit Word")
        print("4. Display Words")
        print("5. Search Word")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            word = input("Enter the word to add: ")
            add_word(word)
        elif choice == '2':
            word = input("Enter the word to delete: ")
            delete_word(word)
        elif choice == '3':
            word = input("Enter the word to edit: ")
            edit_word(word)
        elif choice == '4':
            display_words()
        elif choice == '5':
            word = input("Enter the word to search: ")
            search_word(word)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the CLI menu
if __name__ == "__main__":
    cli_menu()