


def main():

    book = "books/frankenstein.txt"
    text = get_book_path(book)
    num_words = get_num_words(text)
    num_letter = get_num_letters(text)
    sort_dict = sort_on(num_letter)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There are {num_words} words found in this book")
    print("")

    for each in sort_dict:
        print(f"The letter '{each["name"]}' was found {each["num"]} times")

    print("--- End Report ---")

def sort_on(dict):

    list_of_dicts = []
    for each in dict:
        list_of_dicts.append({'name': each, 'num': dict[each]})
    
    list_of_dicts.sort(reverse=False, key=lambda x: x["name"])
    return list_of_dicts


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_path(path):
    with open(path) as f:
        return f.read()


def get_num_letters(text):
    lowered_string = text.lower()
    letters = {}

    for char in lowered_string:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] =1
    return letters


main()