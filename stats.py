def get_num_words(func):
    return len(func.split())


def get_num_characters(func):
    lowercase_text = func.lower()
    characters = {}
    for character in lowercase_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters


def sort_on(item):
        return item["num"]


def make_sorted_dics(func):
    dic_list = []
    for key, value in func.items():
        if key.isalpha():
            dic = {
                "char": key,
                "num": value
                }
            dic_list.append(dic)
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list