# Mo Jansson
# Turning a string backwards using a while loop

# Get input
original_string = input("Write a short sentence: ")

# Set counter to string length - 1
counter = len(original_string) - 1
reversed_string = ""

# Use a while loop to go backwards
while counter >= 0:
    reversed_string += original_string[counter]
    counter -= 1

# Print the reversed string
print("Reversed string:", reversed_string)
