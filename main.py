import sys

def letter_count(string: str) -> dict:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    letter_counts = dict()

    for letter in alpha:
        count = string.count(letter)
        letter_counts[letter] = count

    return letter_counts

def sort_dict_by_key(input: dict):
    output = [{"letter":key,"count":value} for key,value in input.items()]
    output.sort(reverse=True, key=(lambda d : d.get("count")))
    return output

def main(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        book_string = str(file_contents)
        word_count = len(str(file_contents).split())
        counts = letter_count(book_string)

        print(f"--- Report of {filepath} ---")
        print(f"{word_count} words\n")
        for i in sort_dict_by_key(counts):
            print(f"Letter: {i["letter"]}, Occurred {i["count"]} times")


    return

main(sys.argv[1])
