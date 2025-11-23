def count_chars(filepath):
    
    with open(filepath) as book:
        book_text = book.read()
    
    book_text = book_text.lower()
    char_list = list(book_text)
    char_dict = {}
    
    for char in char_list:
        char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict

def count_words(filepath):
    
    with open(filepath) as book:
        book_text = book.read()
    
    word_list = book_text.split()
    num_words = len(word_list)
    
    return num_words

def sort_dict(filepath):
    
    char_dict = count_chars(filepath)
    dict_list = []

    for char in char_dict:
        new_dict = {
            "char" : char,
            "num" : char_dict[char]
        }
        
        if new_dict["char"].isalpha():
            dict_list.append(new_dict)
    
    sorted_list = sorted(dict_list, key=lambda d: d["num"], reverse = True)

    return sorted_list

    