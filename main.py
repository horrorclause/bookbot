
# Gets the content of a book
def get_book_text(filePath):
    with open(filePath) as f:
        fileContent = f.read()
        return fileContent

def main():
    # Prompts user for relative path to book for analysis
    book = get_book_text(input("Enter relative path to book: "))
    print(book)

main()