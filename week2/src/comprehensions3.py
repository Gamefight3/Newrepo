from helpers import get_words, save_counts


def main():
    counts = {}
    words = get_words("address.txt")
    words = [word.lower() for word in words if len(word) > 4]
    
    counts = {word: words.count(word) for word in words}

    save_counts(counts)


main()
