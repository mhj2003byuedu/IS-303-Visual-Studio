# Mo Jansson
# Samson Sperry
# Matthew Christensen

import random

# This should be a child of A5

# I'm pasting my A5 code in and modifying it to fit the new requirements

# Mo Jansson is adding in intromessage for assignment P2

def introMessage():
    print("Welcome to the Soccer Season Simulator!")
    print("Soccer games cannot end in ties in this simulator.")
    print("Scores are randomly generated between 0 and 4.")
    print("Your team will play several games and we will track wins and losses.")
    print()

    sTeamName = input("Enter the name of your home team: ").title()
    iTotalGames = int(input(f"Enter the number of games that the {sTeamName} played: "))

    return sTeamName, iTotalGames

# Ask the user to enter a home soccer team and how many games said team played
sTeamName, iTotalGames = introMessage()

# Make a dictionary of the teams the home team won or lost against
dTeams = {"Won Against": [], "Lost Against": []}

# Samson Sperry is adding menuReturn for assignment P2
def menuReturn() :
    print("---Menu---")
    print(" 1 - Select/Choose Opponent ") # function #3
    print(" 2 - Simulate a Game") # Function # 4
    print(" 3 - Display Final Record\n") # Function #5

    while True : # Defensive coding to prevent errors, and get menu choice from user
        try :
          nChoice = int(input("Select a Menu Choice: "))
          if nChoice not in [1, 2, 3] :
              raise Exception
          break
        except :
            print("Invalid Input, please enter 1, 2, or 3.")
    return nChoice 

iChoice = menuReturn()

iHomeTeamWins = 0
iHomeTeamLosses = 0

# Import random
# Ask about the teams they play against and randomly generate scores for games they play
# Ensure there are no tie games using a while loop for randint generation
# Use counter to manage number of games played

# Matthew Christensen is making following code(function # 3)
# make the same function of this while loop but with a function that when called and filled with a parameter of the 
# team that when the user selects it will remove it from the options of teams available
# not exactly sure what the instructions are saying but I'll try to automate as best as I can

# the while loop will provide this function with the teams but this will display a menu to choose a team to compare
def chooseTeam(teamChoice = None) :
    # display menu to choose a team from the list of teams that the user entered
    print("\nChoose a team that your home team played against.")
    if teamChoice in lstAwayTeams :
        lstAwayTeams.remove(teamChoice)
    for team in lstAwayTeams :
        print(f'- {team}')
    teamChoice = input("--")
    return teamChoice

# Matthew Christensen
# make a function (function #4) that prevents a random number generator from giving back the same number 
# as the other team out of the two teams received

def randomScores(team1,team2) :
    while score1 == score2 :
        score1 = random.randint(0, 3)
        score2 = random.randint(0, 3)

    if score1 > score2 :
        return "W"
    else :
        return "L"

    
# I'm making these into two while loops so I can put my function in between to choose the team.
iCounter = 0
lstAwayTeams = []
while iCounter < iTotalGames:
    sAwayTeam = input(f"Enter the name of the away team for game {iCounter + 1}: ").title()
    lstAwayTeams.append(sAwayTeam)
    iCounter += 1


iCounter = 0
teamChoice = None
if iChoice == "1" :
    """
     Adding the function right here should work but there is no automation happening and is no different than 
     just hard coding the function especially since it is used once.
     what the function should do is be able to be used to get the home team name and away team name but that 
     would change the logic of the code and the other functions created by Samson and Mo.
     it would require the sTeamName function at the start to use the function and have you choose from all
     available teams that were entered by the user beforehand in order to automate code and save time. I'm not sure what 
     the instructions want necessarily
     """
    sAwayTeam = chooseTeam(teamChoice)
    # Generate scores
    # iHomeScore = random.randint(0, 4)
    # iAwayScore = random.randint(0, 4)
    
    # Make sure there's no tie

    # while iHomeScore == iAwayScore:
    #    iHomeScore = random.randint(0, 4)
    #    iAwayScore = random.randint(0, 4)
if iChoice == "2" :
    sWinLoss = randomScores(sTeamName,sAwayTeam)
    # Append to dictionary and update wins/losses
    if sWinLoss == "W" :
        dTeams["Won Against"].append(sAwayTeam)
        iHomeTeamWins += 1
        print(f'The {sTeamName} won against the {sAwayTeam}')
    else:
        dTeams["Lost Against"].append(sAwayTeam)
        iHomeTeamLosses += 1
        print(f'The {sTeamName} lost against the {sAwayTeam}')
        
    # print(f'The {sTeamName} won against the {sAwayTeam}' if iHomeScore > iAwayScore else f'The {sTeamName} lost against the {sAwayTeam}')
        # Print necessary information about the game
    # print(f"{sTeamName}'s score: {iHomeScore} - {sAwayTeam}'s score: {iAwayScore}")
    


# After playing all the games print out: Teams won against:
# Then print out the name of each team your home team won against
print("Teams won against:")
for team in dTeams["Won Against"]:
    print(team)


# Print out: Teams lost against:
# Then print out the name of each team your home team won against.
print("Teams lost against:")
for team in dTeams["Lost Against"]:
    print(team)


# Print out Final season record: <number of wins> - <number of losses>
print(f"Final season record: {iHomeTeamWins} - {iHomeTeamLosses}")


# After all of this, print out a final message based on the record of the home team.
# If they won at least 75% of their games, print out:
# Qualified for the NCAA Soccer Tournament!
# If the team won at least 50% but less than 75% then print out:
# You had a good season.
# Otherwise print out:
# Your team needs to practice!
fWinPercentage = iHomeTeamWins / iTotalGames if iTotalGames > 0 else 0
if fWinPercentage >= 0.75:
    print("Qualified for the NCAA Soccer Tournament!")
elif fWinPercentage >= 0.5:
    print("You had a good season.")
else:
    print("Your team needs to practice!")