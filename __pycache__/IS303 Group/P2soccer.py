# Mo Jansson

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

iHomeTeamWins = 0
iHomeTeamLosses = 0

# Import random
# Ask about the teams they play against and randomly generate scores for games they play
# Ensure there are no tie games using a while loop for randint generation
# Use counter to manage number of games played
iCounter = 0
while iCounter < iTotalGames:
    sAwayTeam = input(f"Enter the name of the away team for game {iCounter + 1}: ").title()
    
    # Generate scores
    iHomeScore = random.randint(0, 4)
    iAwayScore = random.randint(0, 4)
    
    # Make sure there's no tie
    while iHomeScore == iAwayScore:
        iHomeScore = random.randint(0, 4)
        iAwayScore = random.randint(0, 4)
    
    # Append to dictionary and update wins/losses
    if iHomeScore > iAwayScore:
        dTeams["Won Against"].append(sAwayTeam)
        iHomeTeamWins += 1
    else:
        dTeams["Lost Against"].append(sAwayTeam)
        iHomeTeamLosses += 1

        # Print necessary information about the game
    print(f"{sTeamName}'s score: {iHomeScore} - {sAwayTeam}'s score: {iAwayScore}")
    print(f'The {sTeamName} won against the {sAwayTeam}' if iHomeScore > iAwayScore else f'The {sTeamName} lost against the {sAwayTeam}')
    iCounter += 1


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