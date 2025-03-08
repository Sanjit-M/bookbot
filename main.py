from stats import count
from stats import word_counter
from stats import sorted_list
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
        
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    length = count(text)
    word_count = word_counter(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    sorted_dict = sorted_list(word_count)
    print("============= END ===============")
if __name__=="__main__":
    main()

 
