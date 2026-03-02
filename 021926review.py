# Mo Jansson
# Menu review

# Create a function that displays a menu
# 1. Add
# 2. Delete
# 3. Display
# 4. Exit

def showMenu() :
    print('1. Add')
    print ('2. Delete')
    print ('3. Display')
    print ('4. Exit\n')

    iChoice = int(input("Choice: "))

    if (iChoice !=1 and iChoice !=2 and iChoice !=3 and iChoice !=4):
        print ('Please make a valid choice')
    else:
        return iChoice

myList = []
iMyChoice = 0

while (iMyChoice !=4):
    iMyChoice = showMenu()

    if (iMyChoice == 1):
        value = input("Enter a value to add: ")
        myList.append(value)
        # add to list

    elif (iMyChoice == 2):
        if len(myList) > 0:
            myList.pop()
            print ("Last item deleted")
        else:
            print("List is empty")
        #Delete
    elif (iMyChoice == 3):
        print("List contents: ", myList)
        #display
    elif (iMyChoice == 4):
        print("Exiting program")
        break
# Prompt the user to choose a menu item
# Add - adds a value to the list
# Delete - removes the last element in the list
# Display - shows all elements in the list
# Exit - Gets out of the loop