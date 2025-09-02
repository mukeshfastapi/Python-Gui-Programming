# Traversing the List

shoppingList = ['laptop', 'Earbuds', 'Smartphone']

# Method --1
for i in shoppingList:
    print(i)

print()

# Method -2 using of len() and adding something

for j in range(len(shoppingList)):
    shoppingList[j] = shoppingList[j] + "+"
    print(shoppingList[j])