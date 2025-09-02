# Sorting python list

numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
print(sorted(numbers))

# Method 2 using a callback function to sort the 2nd char of the list element

words = ["aa", "ab", "ac", "ba", "cb", "ca"]

print(sorted(words))

# Using of callback functions to sort the 2nd char of the element
print('Using callback functions....')
print(sorted(words, key= lambda words: words[1]))

# using of named functions to achive the task
def select_second_char(word):
    return word[1]
print()
print(sorted(words, key= select_second_char))