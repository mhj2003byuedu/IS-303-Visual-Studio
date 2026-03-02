# Mo Jansson
# Practicing concepts from Chapter 6
sName = input(" Enter your name: ").title()
iAge = int(input(" Enter your age: "))

# if the age > 60
# print(f' ')
# Name, Dang {age} is old! You probably watched B&W TV
# age < 60 and >= 40
# I love 80s music
# Otherwise 
# Display I love Phineas and Ferb

if iAge >= 60:
    print(f'Dang, {sName}, {iAge} is old! You probably watched B&W TV!')
elif iAge < 60 and iAge >= 40:
    print(f"I love 80s music")
else:
    print(f"I love Phineas and Ferb")


# Gift suggestion program
# Variables
# Determine if girlfriend is injured, likes chocolate, likes flowers)
# Run best option given circumstances determined by variables

bBroken = True
bChoc = False
bFlowers = False

if (bBroken):
    if (bChoc):
        print("Chocolate!")
    elif (bFlowers):
        print("Flowers!")
    else:
        print("Soup!")