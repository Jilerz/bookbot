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
