
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    my_dict = {}
    working_list = text.lower().split()
    for char in working_list:
        for letter in char:
            if letter not in my_dict.keys():
                my_dict[letter] = 1
            else:
                my_dict[letter] += 1
    return my_dict

def sorted_list(mydict):
    def sort_on(items):
        return items["num"]
    list_to_sort = []
    for char, num in mydict.items():
        if not char.isalpha():
            continue
        else:
            new_dict = {"char" : char, "num" : num}
            list_to_sort.append(new_dict)
    list_to_sort.sort(reverse=True, key=sort_on)
    return list_to_sort