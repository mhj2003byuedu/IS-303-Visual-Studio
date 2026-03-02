# Mo Jansson
# Section 3
# A Python program that manages a movie collection
# Using a list of dictionaries, users can add, find, delete, and display movies
# through a menu-driven interface

# Define adn setup a menu function with the 5 options and user-inputted choice

def showMenu() :
    print ('--- Movie Collection Menu ---')
    print ('1 - Add Movie')
    print ('2 - Find Movie')
    print ('3 - Delete Movie')
    print ('4 - Display All Movies')
    print ('5 - Exit')

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print('Invalid choice. Please enter a number between 1 and 5.')
        except:
            print("Please enter a valid number.")

# Define empty movie list (and iMyChoice to work with the menu setup)
lstMovie = []
iMyChoice = 0

# Setup while loop with the menu options 
# 1 prompts user to input movie title, and rating from 0-10 to put in a dictionary and add to lstMovie
# Creates three keys, Title (sMovieTitle), Rating (iMovieRating), and rating category (sRatingCategory)
# Rating input determines the rating category as defined by the exam, stored in sRatingCategory as the third key

while (iMyChoice !=5):

    iMyChoice = showMenu()

    if (iMyChoice == 1):

        sMovieTitle = input("Enter the movie title: ").lower()

        iMovieRating = int(input("Enter your rating (0-10): "))

        if iMovieRating < 0 or iMovieRating > 10:
            print("Invalid rating. Please enter a whole number between 0 and 10.")
            continue
        elif iMovieRating >= 9:
            sRatingCategory = "Chili Pepper"
        elif iMovieRating >= 6:
            sRatingCategory = "Green Chili"
        elif iMovieRating >= 3:
            sRatingCategory = "Green Pepper"
        else:
            sRatingCategory = "Dirt"

        # IF "[MY] CATEGORY DISPLAY TEXT SHOULD SIMPLY BE THE CATEGORY NAME"
        # WHY IS THERE A DISPLAY TEXT COLUMN IN THE EXAM WITH INDICATED TEXT OTHER THAN THE CATEGORY NAME
        # THAT COLUMN IS VERY MISLEADING
        # AND "DISPLAY TEXT" IS NOT MENTIONED ANYWHERE IN OPTION 1
        # So I'm ignoring it
        # We move on :)

        # Append dictionary data to the list
        # Print confirmation
        lstMovie.append({"title": sMovieTitle, "rating": iMovieRating, "category": sRatingCategory})
        print(f'{sMovieTitle.title()} has been added to your collection!')
       

# 2 prompts for the title via user input
# then the inputted title is run through a case-insensitive search in the list of movie dictionaries
    if (iMyChoice == 2):
        search = input("Enter the movie title to search for: ").lower()
        found = False

        for movie in lstMovie:
            if movie["title"] == search:
                print("--- Movie Found ---")
                print("Title:", movie["title"].title())
                print("Rating:", str(movie["rating"]) + "/10")
                print("Category:", movie["category"])
                found = True
                break

        if not found:
            print(f'{search.title()} was not found in your collection.')
    
# 3 is for deleting movies
# User enters a movie title, if movie title is found, user is prompted y/n for deletion
# If movie title is not found, print not found and return to menu

    if (iMyChoice == 3):
        search1 = input("Enter the movie title to delete: ").lower()

        for movie in lstMovie:
            if movie["title"] == search1:
                sAnswer = input(f'Are you sure you want to delete {search1.title()}? (yes/no) ').lower()

                if sAnswer == "yes":
                    lstMovie.remove(movie)
                    print("Movie deleted.")
                else:
                    print("Deletion cancelled.")
                break
        else:
            print(f'{search1.title()} was not found in your collection.')


# 4 is for printing all movie dictionaries if the list isn't empty

    if (iMyChoice == 4):
        if len(lstMovie) == 0:
            print("Your movie collection is empty.")
        else:
            print("List contents: ", lstMovie)

# 5 prints a message when selected, to exit the menu

    if (iMyChoice == 5):
        print("Thanks for using the Movie Collection Manager. Goodbye!")
