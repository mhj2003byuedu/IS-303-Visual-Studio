# Mo Jansson
# Intentionally broken Python program
# Contains: SYNTAX errors, LOGIC errors, and RUNTIME errors

#Syntax
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)  # runtime error if nums is empty

def get_number_list():
    raw = input("Enter numbers separated by commas: ")
    parts = raw.split(",")
    nums = []
    for p in parts:
        nums.append(int(p))  # runtime error if p isn't an int (e.g., "3.5" or "")
    return nums

def main():
    nums = get_number_list()

    if len(nums) == 0:  # syntax error (also intended to be wrong comparison)
        print("You entered nothing, but we'll continue anyway!")

    avg = average(nums)

    # logic error: this condition is backwards for "passing"
    if avg < 70:
        print("PASS")
    else:
        print("FAIL")

    # runtime error: IndexError if fewer than 10 numbers
    print("10th number was:", nums[9])

    # runtime error: ZeroDivisionError always
    x = 10 / 0
    print("This will never print", x)

main()  # syntax error: missing closing parenthesis