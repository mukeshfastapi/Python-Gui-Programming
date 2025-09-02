# Traversing the dictionary
names_dict = {'name':"mukesh", "age": 29}

def traverseDict(dict):
    for key in dict:
        print(key) # it will only traverse the key of dict


traverseDict(names_dict)

print()
def traverseDict(dict):
    for key in dict:
        print(key, dict[key]) # it will only traverse the key & value of dict


traverseDict(names_dict)