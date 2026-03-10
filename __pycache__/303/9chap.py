# Mo Jansson
# Chapter 7 practice
# prompts for the # of teams
# store the team name, wins, and losses
# Process the data
# add # of wins and add # of losses in two variables
# display win/loss pct = #wins / #wins + #losses

iCounter = int(input("Enter the number of teams: "))
lstTeams = []
for i in range(iCounter):
    sTeamName = input("Enter the team name: ")
    iTeamWins = int(input("Enter the number of wins: "))
    iTeamLosses = int(input("Enter the number of losses: "))

# Append dictionary data to the list
lstTeams.append({"Names": sTeamName, "Wins": iTeamWins, "Losses": iTeamLosses})

iTotalWins = 0
iTotalLosses = 0

# Display the data
print ("\nTeam Name\tWins\tLosses")
for Name in lstTeams:
    iTotalWins += Name["Wins"]
    iTotalLosses += Name["Losses"]

if (iTeamWins + iTeamLosses) > 0:
    fWinLossPct = iTotalWins / (iTotalWins + iTotalLosses)
else:
    fWinLossPct = 0

print(f'Win %: {fWinLossPct:.3%}')