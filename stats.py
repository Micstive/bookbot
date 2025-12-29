def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    char_count_dict = {}
    for char in text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def get_sorted(char_count_dict):
    dict_list = []
    for key in char_count_dict:
        dict_list.append({"char": key, "num": char_count_dict[key]})
    dict_list.sort(key=lambda d: d["num"], reverse=True)
    return dict_list
