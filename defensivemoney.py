# Mo Jansson
# Working with currency conversion
# None of this code can have try/except statements. It has to use if statements

conversion_rates = { 
 "EUR": 0.93, # Euro 
 "GBP": 0.81, # British Pound 
 "JPY": 133.0, # Japanese Yen 
 "INR": 82.5, # Indian Rupee 
 "AUD": 1.48, # Australian Dollar 
 "CAD": 1.36, # Canadian Dollar 
 "CHF": 0.92, # Swiss Franc 
 "CNY": 7.15, # Chinese Yuan 
 "SEK": 10.5, # Swedish Krona 
 "NZD": 1.62, # New Zealand Dollar 
 "MXN": 18.0, # Mexican Peso 
 } 

# Improper dollar amount
# You need to check if the input from the user can be a valid float before converting it using the .isdecimal() function
# If an invalid value for a float is entered, you should print out:
# <dollar input> is not a valid number. Please try again.
# Then, restart gathering inputs from the start. You should continually ask for a dollar amount until a proper one is provided.
# Function to check if input is a valid float (including negative numbers)
def is_valid_float(s):
    s = s.strip()
    if s.count('.') > 1:
        return False
    if s.startswith('-'):
        s = s[1:]  # remove leading negative for digit check
    return s.replace('.', '', 1).isdigit()

while True:
    # 1. Get a dollar amount from the user
    sAmount = input("Enter an amount in US dollars: ").strip()

    # Check if the input is a valid float
    if is_valid_float(sAmount):
        fAmount = float(sAmount)
    else:
        print(f"{sAmount} is not a valid number. Please try again.")
        continue  # restart loop from the beginning

# You also need to ensure that the inputted currency actually exists in the conversion_rates dictionary. You might find the dictionary .get() function useful. You could also use in with an if statement. How you do it is up to you.
# When an invalid value for a currency is entered, you should print out:
# <entered currency variable> is not a valid currency. Please try again.
# For example, LOL is not a valid currency. Please try again.
# IMPORTANT: Then, restart gathering inputs from the VERY BEGINNING, meaning ask for a dollar amount again
    print("Foreign currencies available for conversion are:")
    print(" ".join(conversion_rates.keys()))
    
    sCurrency = input("Please enter a target currency (e.g., EUR, GBP): ").strip().upper()

    if sCurrency in conversion_rates:
        converted_amount = fAmount * conversion_rates[sCurrency]
        print(f"{fAmount:.2f} USD is equal to {converted_amount:.2f} {sCurrency}")
        break 
    else:
        print(f"{sCurrency} is not a valid currency. Please try again.")
        continue 