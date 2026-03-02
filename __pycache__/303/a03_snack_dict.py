# Mo Jansson
# Making a snack dictionary, then messing with it

dictSnacks = {
    "cheezits": 4,
    "hohos": 6,
    "apples": 3
}

# Print dictionary
print("Current snack inventory: ", dictSnacks)


# Add an item to the dictionary via user input, print again
sNewSnack = str(input("Enter the name of a new snack to add: ").lower())
if sNewSnack in dictSnacks:
    print(sNewSnack.title(), "is already in the snack inventory.")
else:
    iNewQuantity = int(input(f"Enter the quantity of {sNewSnack.lower()} to add: "))
    dictSnacks[sNewSnack] = iNewQuantity
    print(sNewSnack.title(), "was added to your inventory.")


# Update the count for an existing snack
sUpdateSnack = str(input("Enter the name of a snack to update the quantity: ").lower())
if sUpdateSnack in dictSnacks:
    iUpdatedQuantity = int(input(f"Enter the new quantity for {sUpdateSnack.lower()}: "))
    dictSnacks[sUpdateSnack] = iUpdatedQuantity
    print(f"The count for {sUpdateSnack.lower()} was updated.")
else:
    print(sUpdateSnack.title(), "is not in your snack inventory.")


# Remove a snack by name via user input, then print for clarity
sRemoveSnack = str(input("Enter the name of a snack to remove from the inventory: ").lower())
if sRemoveSnack in dictSnacks:
    dictSnacks.pop(sRemoveSnack)
    print(sRemoveSnack.title(), "was removed from the inventory.")
else:
    print(sRemoveSnack.title(), "is not in your snack inventory.")


# Print final dictionary
print("Final snack inventory:", dictSnacks)