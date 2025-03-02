# Splits the book into a list and counts the individual words
def book_word_count(book):
    return len(book.split())

# Counts the individual characters present in the book
def book_char_count(book):
    character_count = {}

    for character in book:
        if str(character.lower()) in character_count:
            character_count[character.lower()] += 1

        else:
            character_count[character.lower()] = 1
    
    return character_count


# Iterates over the dictionary with characters and counts, and splits the individual \
# character and corresponding count into its own dictionary and then sorted by 'count' 
def sort_dicts(dict):
    list_of_dicts = []
    
    for key, value in dict.items():

        # We only want alphabetical characters
        if key.isalpha():
            temp_dict = {}
            temp_dict["character"]= key
            temp_dict["count"]=value
            list_of_dicts.append(temp_dict)

    # Returns the counts value of a character
    def sort_on(d):
        return d["count"]
    
    # Sorts the list of dictionaries by the character counts 'sort_on' function
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts
