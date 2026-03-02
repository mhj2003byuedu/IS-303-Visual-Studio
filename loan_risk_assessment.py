# Mo Jansson
# A program determining loan risk based on inputs by the user
# Variable inputs below
sFirstName = input("Enter your first name: ").title()
sLastName = input("Enter your last name: ").title()
iAnnualIncome = float(input("Enter your annual income: "))
iMonthlyPayment = float(input("Enter the monthly payment: "))

# Debt-to-income Ratio (Monthly debt/(annual income/12))
fDTI = round((float(iMonthlyPayment/(iAnnualIncome/12))),2)

# DTI Ratio Category
if fDTI < 0.2:
    sCat = "Low Risk"
elif 0.2 <= fDTI < 0.36:
    sCat = "Moderate Risk"
elif 0.36 <= fDTI < 0.5:
    sCat = "Elevated Risk"
elif fDTI >= 0.5:
    sCat = "High Risk"

# Execute print
print(f'{sFirstName} {sLastName} has a DTI of {fDTI}. The associated category is: {sCat}.')