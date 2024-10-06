# Project Dictionary
---

*README shamelessly AI-Generated*

<!-- I need your guidance for this project im building. I am creating a python program for a *word dictionary.* 
Here's the kicker:
The program itself is in python.
It contains an interactive menu in CLI.
You should know that the words themselves are stored in the data type dictionary. -->

### **1. Define the Project**
   - **Goal**: Build a Python program that acts as a word dictionary with options to add, delete, edit, display, and search words, depending on their part of speech.
   - **Key Features**:
     - Command-line interface (CLI) with a menu for interaction.
     - Store words based on part of speech (noun, verb, adjective, adverb).
     - Input validation and error handling.

### **2. Design the Program Structure**
   - **Data Storage**: Use a dictionary to store words, with each word having properties like meaning, part of speech, and specific forms (e.g., tenses, singular/plural).
     - Example: 
       ```python
       word_dict = {
           "brave": {
               "meaning": "showing courage",
               "part_of_speech": "adjective",
               "comparative": "braver",
               "superlative": "bravest",
               "examples": {...}
           }
       }
       ```

   - **CLI Menu**:
     - Create a simple menu for users to interact with:
       ```plaintext
       1. Add Word
       2. Delete Word
       3. Edit Word
       4. Display Words
       5. Search Word
       Enter your choice:
       ```
### **3. Develop Core Functions**
   - **Step 1**: Implement the `add_word()` function.
     - Collect the word, meaning, part of speech, and extra details depending on the part of speech.
     - Store everything in the dictionary.

   - **Step 2**: Implement the `delete_word()` function.
     - Ask for the word and remove it from the dictionary if it exists.

   - **Step 3**: Implement the `edit_word()` function.
     - Allow the user to modify the meaning, part of speech, or other properties of a word.

   - **Step 4**: Implement the `display_words()` function.
     - Show all words in the dictionary, sorted in ascending or descending order.

   - **Step 5**: Implement the `search_word()` function.
     - Allow the user to search for a specific word and display its details.

### **4. Add Input Validation**
   - Ensure the program handles invalid inputs smoothly:
     - Check if the word already exists before adding.
     - Validate the part of speech entered by the user.
     - Handle empty inputs or invalid data.
     - 
### **5. Test Each Function**
   - **Test Adding Words**: Add multiple words of different parts of speech.
   - **Test Deleting Words**: Try deleting words and confirm they’re removed.
   - **Test Editing Words**: Edit existing words and ensure changes are applied.
   - **Test Display and Search**: Display and search for words, checking the output.

### **6. Optional Enhancements**
   - **Save to File**: Allow the program to save the dictionary to a file (e.g., JSON) so the data persists after closing the program.
   - **Load from File**: Load the dictionary from a file when the program starts.

### **7. Finalize**
   - **Refine the CLI**: Make sure the menu is clear and easy to navigate.
   - **Error Handling**: Ensure that invalid inputs or actions are handled gracefully (e.g., trying to delete a non-existent word).
   - **Polish the Output**: Format the displayed words in a clean and readable way.

---

## Pseudocode

### 1) **Add Word** Function:

```plaintext
FUNCTION add_word()
    PROMPT user for word
    PROMPT user for meaning/definition
    PROMPT user for part of speech (noun, verb, adjective, adverb)
    
    IF part_of_speech == "noun" THEN
        PROMPT user for singular form of the noun
        PROMPT user for an example sentence using the singular form
        PROMPT user for plural form of the noun
        PROMPT user for an example sentence using the plural form
        
        STORE word, part_of_speech, meaning, singular form, plural form, and example sentences in the dictionary

    ELSE IF part_of_speech == "verb" THEN
        PROMPT user for past tense of the verb
        PROMPT user for an example sentence using the past tense
        PROMPT user for present tense of the verb
        PROMPT user for an example sentence using the present tense
        PROMPT user for future tense of the verb
        PROMPT user for an example sentence using the future tense
        
        STORE word, part_of_speech, meaning, past tense, present tense, future tense, and example sentences in the dictionary

    ELSE IF part_of_speech == "adjective" THEN
        PROMPT user for comparative form of the adjective
        PROMPT user for an example sentence using the comparative form
        PROMPT user for superlative form of the adjective
        PROMPT user for an example sentence using the superlative form
        
        STORE word, part_of_speech, meaning, comparative, superlative, and example sentences in the dictionary

    ELSE IF part_of_speech == "adverb" THEN
        PROMPT user for comparative form of the adverb
        PROMPT user for an example sentence using the comparative form
        PROMPT user for superlative form of the adverb
        PROMPT user for an example sentence using the superlative form
        
        STORE word, part_of_speech, meaning, comparative, superlative, and example sentences in the dictionary

    ELSE
        DISPLAY "Invalid part of speech."

    END IF
END FUNCTION
```

### Key Steps in the Pseudocode:
1. **Prompting for word, meaning, and part of speech**: Begin by asking the user to input the necessary details.
2. **Conditional branches based on part of speech**: Depending on whether the word is a noun, verb, adjective, or adverb, ask for specific information such as singular/plural forms, tenses, or comparative/superlative forms.
3. **Storing the word in the dictionary**: After collecting all the necessary information, store the word and its related data into the `dictionary` structure.

Here’s the pseudocode for the remaining functions (2-5):

### 2) **Delete Word** Function:

```plaintext
FUNCTION delete_word()
    PROMPT user for the word to delete
    
    IF word exists in dictionary THEN
        DELETE word from dictionary
        DISPLAY "Word deleted successfully."
    ELSE
        DISPLAY "Word not found in the dictionary."
    END IF
END FUNCTION
```

### Key Steps:
1. **Prompt for the word**: Ask the user for the word they want to delete.
2. **Check if the word exists**: Use an `if` condition to check if the word is in the dictionary.
3. **Delete the word**: If the word exists, remove it using `del` or `pop()`. Otherwise, notify the user that the word isn't found.

### 3) **Edit Word** Function:

```plaintext
FUNCTION edit_word()
    PROMPT user for the word to edit
    
    IF word exists in dictionary THEN
        DISPLAY current information (meaning, part of speech, forms, tenses, etc.)
        PROMPT user for the aspect they want to edit (meaning, part of speech, forms, tenses, etc.)
        
        IF user chooses "meaning" THEN
            PROMPT for the new meaning
            UPDATE word's meaning in the dictionary
        
        ELSE IF user chooses "part of speech" THEN
            PROMPT for the new part of speech
            PROMPT for corresponding new forms/tenses based on the new part of speech
            UPDATE the word's forms/tenses accordingly in the dictionary
            
        ELSE IF user chooses to edit specific forms/tenses THEN
            PROMPT for the new forms/tenses based on the part of speech
            UPDATE specific forms/tenses in the dictionary
        
        END IF
        
        DISPLAY "Word edited successfully."
    ELSE
        DISPLAY "Word not found in the dictionary."
    END IF
END FUNCTION
```

### Key Steps:
1. **Prompt for the word to edit**: Ask the user which word they want to edit.
2. **Show current information**: Display the existing details about the word.
3. **Choose what to edit**: Ask what aspect the user wants to edit (meaning, part of speech, forms/tenses).
4. **Edit based on input**: Update the specific data in the dictionary depending on the user's choice.

### 4) **Display Words** Function:

```plaintext
FUNCTION display_words()
    PROMPT user for sorting order (ascending or descending)
    
    IF user chooses ascending THEN
        SORT dictionary keys in ascending order
    ELSE IF user chooses descending THEN
        SORT dictionary keys in descending order
    END IF
    
    FOR each word in the sorted dictionary
        DISPLAY word, part of speech, meaning, and any additional forms/tenses with example sentences
    END FOR
END FUNCTION
```

### Key Steps:
1. **Prompt for sorting order**: Ask the user if they want to display the words in ascending or descending order.
2. **Sort dictionary keys**: Use `sorted()` to arrange the words accordingly.
3. **Loop through sorted words**: Display each word's details, including part of speech, meaning, and any forms/tenses.

### 5) **Search Word** Function:

```plaintext
FUNCTION search_word()
    PROMPT user for the word to search
    
    IF word exists in dictionary THEN
        DISPLAY word, part of speech, meaning, and any additional forms/tenses with example sentences
    ELSE
        DISPLAY "Word not found in the dictionary."
    END IF
END FUNCTION
```
### Key Steps:
1. **Prompt for the word**: Ask the user which word they want to search.
2. **Check if the word exists**: Use an `if` condition to see if the word is in the dictionary.
3. **Display word details**: If found, show all relevant information. If not found, notify the user.
