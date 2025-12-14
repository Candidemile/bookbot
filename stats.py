def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def get_words_num(text):
    total_words = text.split()
    return len(total_words)


def get_char_count(text):
    text = text.lower()
    count_dict = {}
    for e in text:
        if e in count_dict:
            count_dict[e] += 1
        else:
            count_dict[e] = 1
    return count_dict


def sort_on(items):
    return items["num"]


def get_sorted_char_list(char_dict):
    list = []
    for item in char_dict:
        list.append({"char": item, "num": char_dict[item]})
    list.sort(reverse=True, key=sort_on)
    return list
