# Finding the length of the user input string , Rule 1- use of split() and Len()
def find_length_of_input(userinput):

    items = userinput.split()

    return len(items)

print(find_length_of_input("mukesh"))