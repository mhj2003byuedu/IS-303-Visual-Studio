# Mo Jansson
# This document contains the functions for the function smorgasbord assignment

# This function adds together 2 numbers and returns the result
def sum_two_numbers(a, b):
    """
    This function takes two numbers as arguments, adds them together, and returns the result.
    :param a: A number (could be integer or float).
    :param b: Another number (could be integer or float).
    :return: The sum of a and b.
    """
    return a + b



# A function that tells you if a number is even or odd
# Argument "num" has to be an integer
# Then returns boolean "true" if the number is even, and "false" if the number is odd
def is_even(num):
    """
    This function takes an integer as an argument and returns True if the number is even, and False if the number is odd.
    :param num: An integer number.
    :return: True if num is even, False if num is odd.
    """
    return num % 2 == 0


# returns a message telling you whether an integer is even or odd
# Uses the is_even function to do so
def get_number_parity(num):
    """
    This function takes an integer as an argument and returns a message indicating whether the number is even or odd.
    :param num: An integer number.
    :return: A string message indicating if num is even or odd.
    """
    if is_even(num):
        return f"{num} is even."
    else:
        return f"{num} is odd."
    


# This function converts a temperature in Fahrenheit to Celsius
# parameters:fahrenheit (an integer or float expressing a temperature in Fahrenheit)
# The function should take the fahrenheit parameter and convert it to Celsius using this formula:
# °C = (°F - 32) * (5/9)
# Then return the Celsius value

def fahrenheit_to_celsius(fahrenheit):
    """
    This function takes a temperature in Fahrenheit as an argument, converts it to Celsius, and returns the Celsius value.
    :param fahrenheit: A number (integer or float) representing a temperature in Fahrenheit.
    :return: The equivalent temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius




# A function that shows the smallest number, biggest number, and mean when given a list of numbers.
# parameter "numbers_list" is a list that contains only integers or floats.
# The function should return a list that has the lowest number in the first position, the highest number in the second position, and the mean of all numbers in the third position
# [<lowest number>, <highest number>, <mean>]
def min_max_mean(numbers_list):
    """
    This function takes a list of numbers as an argument and returns a list containing the smallest number, the largest number, and the mean of the numbers.
    :param numbers_list: A list of numbers (integers or floats).
    :return: A list in the format [<lowest number>, <highest number>, <mean>].
    """
    lowest = min(numbers_list)
    highest = max(numbers_list)
    mean = sum(numbers_list) / len(numbers_list)

    return [lowest, highest, mean]



# Function dog_message returns a message about a dog and its age.
# parameter 1, name, is a string representing the dog’s name.
# parameter 2, age, is an integer representing the dog’s age. It should have a default value of 0.
# The function should return a string that includes the parameters for the dog’s name and age. Make sure the age displays as 0 if no argument for age is provided.
# Print the message in the format: I am a dog named <name> and I'm <age> years old!

def dog_message(name, age=0):
    """
    This function takes a dog's name and age as arguments and returns a message about the dog. The age parameter has a default value of 0.
    :param name: A string representing the dog's name.
    :param age: An integer representing the dog's age (default is 0).
    :return: A string message in the format: "I am a dog named <name> and I'm <age> years old!"
    """
    return f"I am a dog named {name} and I'm {age} years old!"


# Function classify_age returns a string that classifies an age into one of 3 groups.
# parameter 1, age, is an integer representing a person’s age
# parameter 2, senior_age, is an integer representing the age at which someone is considered a “Senior”. It should have a default value of 65.
# The function should reference the age provided and return a string based on how old the person is.
# If the age is below 18, it should return the string Minor.
# If age is below the senior_age, it should return the string Adult
# If the age is equal to or above the senior_age, it should return the string Senior.

def classify_age(age, senior_age=65):
    """
    This function takes a person's age and classifies it into one of three groups: Minor, Adult, or Senior. The senior_age parameter has a default value of 65.
    :param age: An integer representing a person's age.
    :param senior_age: An integer representing the age at which someone is considered a "Senior" (default is 65).
    :return: A string classification of the age group ("Minor", "Adult", or "Senior").
    """
    if age < 18:
        return "Minor"
    elif age < senior_age:
        return "Adult"
    else:
        return "Senior"
    

# a function that calculates the total amount paid for a quantity of a product based on the quantity being bought, the discount percent, and whether a bonus discount is applied.
# The function should calculate the total price (price * quantity), and depending on the total price, the discount will be different
# If the total price is equal to or below the threshold_total, then the discount applied would just be the discount_percent.
# If the total price is above the threshold_total, then the applied discount should be the discount_percent + bonus_discount
# Return the total price, rounded to the second decimal, after the discount is applied. Your return value should just be a float.

def calculate_total(price, quantity, discount_percent, threshold_total=100, bonus_discount=0.02):
    """
    This function calculates the total amount paid for a quantity of a product based on the price, quantity, discount percent, and whether a bonus discount is applied.
    :param price: A number representing the price of a single product.
    :param quantity: An integer representing how many units of the product are being purchased.
    :param discount_percent: A float representing the base discount as a decimal (e.g., 0.1 for 10%).
    :param threshold_total: A number representing the threshold for total price to apply bonus discount (default is 100).
    :param bonus_discount: A float representing the bonus discount as a decimal (default is 0.02).
    :return: The total price after discount, rounded to two decimal places.
    """
    total_price = price * quantity

    if total_price > threshold_total:
        total_discount = discount_percent + bonus_discount
    else:
        total_discount = discount_percent

    discounted_price = total_price * (1 - total_discount)
    return round(discounted_price, 2)
