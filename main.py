def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    character_count = count_unique_characters(book_text)

    unique_character_count = convert_dict(character_count)
    unique_character_count.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for c in unique_character_count:
        if c["char"].isalpha():
            print(f"The {c["char"]} character was found {c["num"]} times")
    print("--- End report ---")

#Sort dictionary list
def sort_on(dict):
    return dict["num"]

#Convert dictionary into a list of dictionaries
def convert_dict(dict):
    converted_list = []
    for k in dict:
        new_dict = {}
        new_dict["char"] = k
        new_dict["num"] = dict[k]
        converted_list.append(new_dict)
    return converted_list

# Read the text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Count the words from any text
def count_words(text):
    words = text.split()
    return len(words)

# Count the amount of times a character appears in a text
def count_unique_characters(text):
    character_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1

    return character_count

main()