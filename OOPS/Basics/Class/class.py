class Myclass:
    language = 'Python'
    version = "3.12"


print(getattr(Myclass, 'language'))

# Exception
# print(getattr(Myclass, 'X'))

# Handling
print(getattr(Myclass, 'X', 'N/A'))