# Mo Jansson
# Primary document for the function smorgasbord assignment

# Import functions from a6functions.py and operator
from operator import call
from a6functions import (sum_two_numbers)
from a6functions import (is_even)
from a6functions import (get_number_parity)
from a6functions import (fahrenheit_to_celsius)
from a6functions import (min_max_mean)
from a6functions import (dog_message)
from a6functions import (classify_age)
from a6functions import (calculate_total)
# from a6functions import (welcome_message)
# Line above is commented out because welcome_message is used in this document and not in a6functions.py, so it would cause an error if we tried to import it from there.

# First, print out a simple message with a person’s name
def welcome_message(name):
    """
    This function takes a name as an argument and prints out a welcome message.
    :param name: A string containing a name.
    :return: None
    """
    print(f"Hello {name}, welcome to IS 303!")


# Call welcome_message with “Diego” as an argument, and then call it again with “Mai” as an argument
name1 = call(welcome_message, "Diego")
name2 = call(welcome_message, "Mai")


# Use the call function on sum_two_numbers with 5 and 7 as arguments, and print the result
result1 = call(sum_two_numbers, 5, 7)
print(result1)



# Then call sum_two_numbers again with 1000.5 and -30 as arguments, and print the result
result2 = call(sum_two_numbers, 1000.5, -30)
print(result2)



# call is_even with the number 7 and print out the result
# Then call it again with the number 120 and print the result

even1 = call(is_even, 7)
print(even1)

even2 = call(is_even, 120)
print(even2)



# call get_number_parity function with 5 as the argument and print out the result
# Then call it again with the number 10 and print the result

parity1 = call(get_number_parity, 5)
print(parity1)

parity2 = call(get_number_parity, 10)
print(parity2)



# call the function with 32 as the argument and print out the returned value
# Then call it with 75 as the argument and print out the returned value

celsius1 = call(fahrenheit_to_celsius, 32)
print(round(celsius1, 2))

celsius2 = call(fahrenheit_to_celsius, 75)
print(round(celsius2, 2))


# call numbers_list_1 using the list as an argument, and print out the result:
numbers_list_1 = call(min_max_mean, [20, 45, 23, 2, 87, 3])
print(numbers_list_1)



# call the function twice, once using "Spot" for the name and 7 for the age
# and another time using just "Peppy" for the name. Print out the returned values.

dog_message_1 = call(dog_message, "Spot", 7)
print(dog_message_1)

dog_message_2 = call(dog_message, "Peppy")
print(dog_message_2)



# Call the function twice, once using 60 for the age and 55 for the senior_age
# Call the function another time using just 62 for the age. Print out the returned values

age_class_1 = call(classify_age, 60, 55)
print(age_class_1)

age_class_2 = call(classify_age, 62)
print(age_class_2)


# write a loop that runs 2 times
# In each iteration, ask the user to input a price and the quantity of a product purchased
# Also ask for a discount percent (formatted as a decimal, so 20% would be processed as 0.20)
# Then call the function using the price, quantity, and discount_percent gathered and print out a message using the returned float that shows the total:
# The total price after discounts is: $<total price returned from calculate_total>
for i in range(2):
    price = float(input("Enter the price for the product purchased: "))
    quantity = int(input("Enter the quantity of the product purchased: "))
    discount_percent = float(input("Enter the discount percent (formatted as a decimal): "))
    total = call(calculate_total, price, quantity, discount_percent)
    print(f"The total price after discounts is: ${total}")