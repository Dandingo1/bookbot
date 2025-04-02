def get_word_count(book_text):
    word_arr = book_text.split()
    return len(word_arr)

def get_character_count(book_text):
    character_count_dict = {}
    for character in book_text:
        temp = character.lower()
        if temp in character_count_dict:
            character_count_dict[temp] += 1
        else:
            character_count_dict[temp] = 1
    return character_count_dict

def sort_on(dict):
    return dict["value"]

def sort_character_dict(character_dict):
    dict_arr = []
    for item in character_dict:
        if item.isalpha():
            dict_arr.append({"character": item, "value": character_dict[item]})
    dict_arr.sort(reverse=True, key=sort_on)
    return dict_arr


    