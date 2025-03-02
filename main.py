# Gets the content of a book and count of all the words

from stats import book_word_count, book_char_count, sort_dicts

#bookPath = input("Enter relative path to book: ") This is to remove hardcoded paths to books
bookPath = "books/frankenstein.txt"

def get_book_text(filePath):
    with open(filePath) as f:
        fileContent = f.read()
        return fileContent  


def main():

    book = get_book_text(bookPath)
    # Grabs total word count from book
    wordCount = book_word_count(book)
    # Counts of individual characters
    charCount = book_char_count(book)
    #Sorts and returns the character counts, takes charCount dicitionary as input
    dictSorted = sort_dicts(charCount)

    print("=========== BookBot ===========")
    print(f"Analyzing the book located at {bookPath}...\n")
    print("--------- Word Count ---------")
    print(f"Found {wordCount} total words\n")
    print("------ Character Count ------")
    #print(f"{charCount}\n")
    for entry in dictSorted:
        print(f"{entry["character"]}: {entry["count"]}")


main()