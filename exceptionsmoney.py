# Mo Jansson
# Working with currency conversion

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


# 1. Get a dollar amount from the user
# Ask the user: Enter an amount in US dollars:
# Make sure that the code will work even if they enter extra spaces before or after the dollar currency
# For example, "30.5" and " 30.5 " should both work
# That amount should be converted to a float datatype
sAmount = input("Enter an amount in US dollars: ")
sAmount = sAmount.strip() 
fAmount = float(sAmount)


# 2. Display available currencies
# Then the program needs to print out all the currencies available to convert to, like this:
# Foreign currencies available for conversion are:
# EUR GBP JPY INR AUD CAD CHF CNY SEK NZD MXN
print("Foreign currencies available for conversion are:")
for currency in conversion_rates.keys():
    print(currency, end=" ")
print() # Print a newline at the end


# 3. Get a target currency to convert to
# Then the program will ask the user:
# Please enter a target currency (e.g., EUR, GBP):
# Make it so that even if the user enters a correctly spelled currency in lowercase or with extra space before or after, it would still work
# For example, " eur " should be the same as "EUR". Input test case 2 specifically will enter a lowercase input with extra spaces before and after, and that should be considered a valid input.
sCurrency = input("Please enter a target currency (e.g., EUR, GBP): ")
sCurrency = sCurrency.strip().upper()


# Your program should then convert the amount in US dollars to an amount in whatever currency was entered
# Do this by multiplying the amount of US dollars by the exchange rate listed in the provided conversion_rates dictionary.
# Validate the target currency and display the result with try/except structure
try:
    conversion_rate = conversion_rates[sCurrency]
    converted_amount = fAmount * conversion_rate
    print(f"{fAmount:.2f} USD is equal to {converted_amount:.2f} {sCurrency}")
except KeyError:
    print(f"{sCurrency} is not a valid currency. Please try again.")