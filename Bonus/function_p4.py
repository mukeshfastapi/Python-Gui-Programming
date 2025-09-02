# Find the average of the list using a function

def average(mylist):
    # Logic : sum of list / len of list
    avg = sum(mylist) / len(mylist)
    return avg


print(average([10,20,30]))