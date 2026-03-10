# Mo Jansson
# Chapter 5 practice with inputs, formatting, rounding, and assignments
# prompts the user to enter in a full name
# Birth year, sum of all the test scores
# number of tests
# do this for two students
# Display name in uppercase born in year scored sum points on #test for an average of avg %

sNameOne = input("Enter a first and last name: ").title()
iOneBirthYear = int(input("Enter the birth year of person 1: "))
sNameTwo = input ("Enter a different first and last name: ").title()
iTwoBirthYear = int(input("Enter the birth year of person 2: "))
iOneNumberOfTests = 2
iTwoNumberOfTests = 4
iOneSumTestScores = (503.82)
iTwoSumTestScores = (609.3)
fOneAverage = (iOneSumTestScores / iOneNumberOfTests)
fTwoAverage = (iTwoSumTestScores / iTwoNumberOfTests)
print(f'{sNameOne} born in {iOneBirthYear} scored {iOneSumTestScores} points on {iOneNumberOfTests} tests for an average of {round(fOneAverage, 2)}')
print(f'{sNameTwo} born in {iTwoBirthYear} scored {iTwoSumTestScores} points on {iTwoNumberOfTests} tests for an average of {round(fTwoAverage, 2)}')


