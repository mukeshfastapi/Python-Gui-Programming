# Creating 1st Node class constructor

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Creating 1st object
new_node = Node(10)

print(new_node)
