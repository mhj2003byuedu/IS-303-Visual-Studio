# Mo Jansson
# Creating a grocery python list and messing with it

# Add 3 foods to list
listGroceries = []
listGroceries.append("Milk")
listGroceries.append("Eggs")
listGroceries.append("Bread")

# Print list
print("Current grocery list:", listGroceries)

# Add an item to the list via user input, print again
listGroceries.append(input("Enter a new grocery item to add: ").title())
print("Current grocery list:", listGroceries)

# Have user check and see if an item is on the list, then print for clarity
sCheck = str(input("Enter the name of an item to check if it's on the list: ").title())
if sCheck in listGroceries:
    print(sCheck, "is on the grocery list.")
else: 
    print(sCheck, "is not on the grocery list.")

# If an item is on the list, a user can remove it via input, then print for clarity
sRemove = str(input("Enter an item to remove from the list: ").title())
if sRemove in listGroceries:
    listGroceries.remove(sRemove)
    print(sRemove, "was removed from the list.")
else:
    print(sRemove, "is not in your list.")

# Remove the first item from the list, print for clarity
removedItem = listGroceries.pop(0)
print(f'The first item, "{removedItem}", was also removed from the list.')

# Print final list
print("Final grocery list:", listGroceries)