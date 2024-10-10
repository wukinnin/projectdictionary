# import word_dict from word_data.py
from word_data import word_dict

##################################################################################
# not present in CLI -- print_word
def print_word(word):
    details = word_dict[word]
    print(f"\n{word}")
    print(f"  Meaning: {details['meaning']}")
    print(F"  Example Sentence: {details['example_sentence']}")
    print(f"  Part of Speech: {details['part_of_speech']}")
    part_of_speech = details['part_of_speech']

    # ADJECTIVE
    if part_of_speech == "adjective":
        print(f"  Comparative: {details['comparative']['form']}")
        print(f"    Sentence: {details['comparative']['sentence']}")
        print(f"  Superlative: {details['superlative']['form']}")
        print(f"    Sentence: {details['superlative']['sentence']}")
        # ADVERB
    elif part_of_speech == "adverb":
        print(f"  Comparative: {details['comparative']['form']}")
        print(f"    Sentence: {details['comparative']['sentence']}")
        print(f"  Superlative: {details['superlative']['form']}")
        print(f"    Sentence: {details['superlative']['sentence']}")
    # NOUN
    elif part_of_speech == "noun":
        print(f"  Singular: {details['singular']['form']}")
        print(f"    Sentence: {details['singular']['sentence']}")
        print(f"  Plural: {details['plural']['form']}")
        print(f"    Sentence: {details['plural']['sentence']}")
    # VERB
    elif part_of_speech == "verb":
        print(f"  Past Tense: {details['tenses']['past']['form']}")
        print(f"    Sentence: {details['tenses']['past']['sentence']}")
        print(f"  Present Tense: {details['tenses']['present']['form']}")
        print(f"    Sentence: {details['tenses']['present']['sentence']}")
        print(f"  Future Tense: {details['tenses']['future']['form']}")
        print(f"    Sentence: {details['tenses']['future']['sentence']}")

##################################################################################        
# 1 - add_word()
def add_word(word):
    # Check if the word already exists in the dictionary
    if word in word_dict:
        print(f"Word '{word}' already exists in the dictionary.")
        return # exit the method
    
    # Get the meaning of the word
    meaning = input(f"Enter the meaning of '{word}': ")
    # Get the example sentence for the word
    example_sentence = input(f"Enter an example sentence for '{word}': ")
    # Get the part of speech
    part_of_speech = input(f"Enter part of speech (noun, verb, adjective, adverb): ")
    # Create the initial word structure
    word_dict[word] = {
        "meaning": meaning,
        "example_sentence": example_sentence,
        "part_of_speech": part_of_speech
    }
    
    # ADJECTIVE
    if part_of_speech == "adjective":
        comparative = input(f"Enter comparative form: ")
        comparative_sentence = input(f"Enter example sentence for comparative form: ")
        superlative = input(f"Enter superlative form: ")
        superlative_sentence = input(f"Enter example sentence for superlative form: ")
        word_dict[word]["comparative"] = {
            "form": comparative,
            "sentence": comparative_sentence
        }
        word_dict[word]["superlative"] = {
            "form": superlative,
            "sentence": superlative_sentence
        }
    # ADVERB
    elif part_of_speech == "adverb":
        comparative = input(f"Enter comparative form: ")
        comparative_sentence = input(f"Enter example sentence for comparative form: ")
        superlative = input(f"Enter superlative form: ")
        superlative_sentence = input(f"Enter example sentence for superlative form: ")
        word_dict[word]["comparative"] = {
            "form": comparative,
            "sentence": comparative_sentence
        }
        word_dict[word]["superlative"] = {
            "form": superlative,
            "sentence": superlative_sentence
        }
    # NOUN
    elif part_of_speech == "noun":
        singular = input(f"Enter singular form: ")
        singular_sentence = input(f"Enter example sentence for singular form: ")
        plural = input(f"Enter plural form: ")
        plural_sentence = input(f"Enter example sentence for plural form: ")
        word_dict[word]["singular"] = {
            "form": singular,
            "sentence": singular_sentence
        }
        word_dict[word]["plural"] = {
            "form": plural,
            "sentence": plural_sentence
        }
    # VERB
    elif part_of_speech == "verb":
        past = input(f"Enter past tense: ")
        past_sentence = input(f"Enter example sentence for past tense: ")
        present = input(f"Enter present tense: ")
        present_sentence = input(f"Enter example sentence for present tense: ")
        future = input(f"Enter future tense: ")
        future_sentence = input(f"Enter example sentence for future tense: ")

        word_dict[word]["tenses"] = {
            "past": {"form": past, "sentence": past_sentence},
            "present": {"form": present, "sentence": present_sentence},
            "future": {"form": future, "sentence": future_sentence}
        }
    print(f"\nWord '{word}' has been added to the dictionary.")

##################################################################################
# 2 - delete_word
def delete_word(word):
    # Check if word does not exist in word_dict
    if word not in word_dict:
        print(f"Word '{word}' not present in dictionary.")
    else:
        del word_dict[word]
        print(f"Word '{word}' is deleted from dictionary")

##################################################################################
# 3 - edit_word
def edit_word(word):
    # Check if word does not exist in word_data
    if word not in word_dict:
        print(f"Word '{word}' not present in dictionary.")
        return # exit the method
    # Get the current details of the word and display
    details = word_dict[word]
    print_word(word)
    
    # Edit the meaning
    new_meaning = input(f"\nEnter new meaning (or press Enter to keep current): ")
    if new_meaning:
        word_dict[word]['meaning'] = new_meaning
    # Edit the example sentence
    new_example = input(f"Enter new example sentence (or press Enter to keep current): ")
    if new_example:
        word_dict[word]['example_sentence'] = new_example

    # Edit the part of speech
    current_part_of_speech = details['part_of_speech']
    new_part_of_speech = input(f"Enter new part of speech \ne.g. adjective, adverb, noun, verb \n(or press Enter to keep current): ")
    if new_part_of_speech:
        word_dict[word]['part_of_speech'] = new_part_of_speech
        part_of_speech = new_part_of_speech
    else:
        part_of_speech = current_part_of_speech
    # Remove old part of speech before updating
    if current_part_of_speech == "adjective" or current_part_of_speech == "adverb":
        word_dict[word].pop('comparative', None)
        word_dict[word].pop('superlative', None)
    elif current_part_of_speech == "noun":
        word_dict[word].pop('singular', None)
        word_dict[word].pop('plural', None)
    elif current_part_of_speech == "verb":
        word_dict[word].pop('tenses', None)

    # ADJECTIVE
    if part_of_speech == "adjective":
        new_comparative = input(f"Enter new comparative form (or press Enter to keep current): ")
        if new_comparative:
            word_dict[word]['comparative'] = {"form": new_comparative, "sentence": input(f"Enter sentence for comparative form: ")}
        new_superlative = input(f"Enter new superlative form (or press Enter to keep current): ")
        if new_superlative:
            word_dict[word]['superlative'] = {"form": new_superlative, "sentence": input(f"Enter sentence for superlative form: ")}
    # ADVERB
    elif part_of_speech == "adverb":
        new_comparative = input(f"Enter new comparative form (or press Enter to keep current): ")
        if new_comparative:
            word_dict[word]['comparative'] = {"form": new_comparative, "sentence": input(f"Enter sentence for comparative form: ")}
        new_superlative = input(f"Enter new superlative form (or press Enter to keep current): ")
        if new_superlative:
            word_dict[word]['superlative'] = {"form": new_superlative, "sentence": input(f"Enter sentence for superlative form: ")}
    # NOUN
    elif part_of_speech == "noun":
        new_singular = input(f"Enter new singular form (or press Enter to keep current): ")
        if new_singular:
            word_dict[word]['singular'] = {"form": new_singular, "sentence": input(f"Enter sentence for singular form: ")}
        new_plural = input(f"Enter new plural form (or press Enter to keep current): ")
        if new_plural:
            word_dict[word]['plural'] = {"form": new_plural, "sentence": input(f"Enter sentence for plural form: ")}
    # VERB
    elif part_of_speech == "verb":
        new_past = input(f"Enter new past tense (or press Enter to keep current): ")
        if new_past:
            word_dict[word]['tenses'] = {"past": {"form": new_past, "sentence": input(f"Enter sentence for past tense: ")}}
        new_present = input(f"Enter new present tense (or press Enter to keep current): ")
        if new_present:
            word_dict[word]['tenses']['present'] = {"form": new_present, "sentence": input(f"Enter sentence for present tense: ")}
        new_future = input(f"Enter new future tense (or press Enter to keep current): ")
        if new_future:
            word_dict[word]['tenses']['future'] = {"form": new_future, "sentence": input(f"Enter sentence for future tense: ")}

    print(f"\nWord '{word}' has been updated.")

##################################################################################
# 4 - display_word()
def display_words():
    # by default: arrange in ascending
    sorted_words = sorted(word_dict.keys()) 
    # loop statement to loop through all the word_data
    for word in sorted_words:
        print_word(word)

##################################################################################
# 5 - search_word()
def search_word(word):
    # Check if word does not exist in word_dict
    if word not in word_dict:
        print(f"Word '{word}' not present in dictionary.")
    else:
        print(f"Word '{word}' is present in dictionary.")
        print_word(word)
    