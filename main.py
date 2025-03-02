# Gets the content of a book and count of all the words
import sys
from stats import book_word_count, book_char_count, sort_dicts


def get_book_text(filePath):
    with open(filePath) as f:
        fileContent = f.read()
        return fileContent  


def main():

    # Checks to see that a file path is provided, if not it exits
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookPath = str(sys.argv[1])
        #print(len(sys.argv), type(sys.argv))


    book = get_book_text(bookPath)
    # Grabs total word count from book
    wordCount = book_word_count(book)

    # Counts of individual characters returns unsorted dictionary
    charCount = book_char_count(book)

    #Sorts and returns the character counts, takes charCount dicitionary as input
    dictSorted = sort_dicts(charCount)

    print("=========== BookBot ===========")
    print(f"Analyzing the book located at {bookPath}...\n")
    print("--------- Word Count ---------")
    print(f"Found {wordCount} total words\n")
    print("------ Character Count ------")
    
    for entry in dictSorted:
        print(f"{entry['character']}: {entry['count']}")

    print("\n============= END =============")


if __name__=='__main__':

    main()