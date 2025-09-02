# searching pairs in a dictionary

names_dict = {'name': "mukesh", "age": 29}

def linearSearch(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value

    return "Item not found "

print(linearSearch(names_dict, 29))

print(linearSearch(names_dict, 290))