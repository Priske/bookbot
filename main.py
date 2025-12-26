from stats import word_count, count_char, sorted_dict
import sys

def get_book_text(booktextPath):
    text = None
    with open(booktextPath) as p:
        text = p.read()
    
    return text

def print_report(bookpath,book,sorted):
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {bookpath}...")
            print("----------- Word Count ----------")
            print(word_count(book))
            print("--------- Character Count -------")
            for char in sorted:
                if(char.isalpha()):
                    print(f"{char[0]}: {sorted[char]}")
            print("============= END ===============")

def main():
    print("Usage: python3 main.py <path_to_book>")
    print (sys.argv)
    if(len(sys.argv) >1):
        sorted={}
        book = get_book_text(sys.argv[1]) 
        sorted = sorted_dict(count_char(book))            
        print_report(sys.argv[1],word_count(book),sorted)
        
       
    else:
        sys.exit(1)
main()