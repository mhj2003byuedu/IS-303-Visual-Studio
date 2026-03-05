# Mo Jansson
# - Notes for new exam

from datetime import datetime

# raw_date = input("enter the haircut date (mm-dd-yyyy): ")

class Stylist:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()

class Haircut:
    def __init__(self, date, haircut_type, tip, stylist):
        self.date = date
        self.haircut_type = haircut_type
        self.tip = tip
        self.employee = stylist

        if haircut_type == "Normal":
            self.cost = 20.00
        else:
            self.cost = 30.00

        self.total_cost = self.cost + self.tip

class Client:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.age = age
        self.haircuts = []

    def print_haircuts(self):
        for haircut in self.haircuts:
            print(f" Haircut | Date: {haircut.date} | Type: {haircut.type} | Cost: {haircut.cost}"
                  f" | Tip: {haircut.tip} | Total: {haircut.total_cost} | Stylist: {haircut.employee.first_name}"
                  f"{haircut.employee.last_name}")
            
def display_menu():
    print("\n--- Barbershop Menu ---")
    print("1 - Add Client and Haircut")
    print("2 - Search for Client")
    print("3 - Stylist Totals (All Clients)")
    print("4 - Exit")
    return input("Choice: ")

def add_client(clients):
    print("\n -- Add Client --")
    first_name = input("Enter the Client's first name: ")
    last_name = input("Enter the Client's last name: ")
    while True:
        try:
            age = int(input("Enter the Client's age: "))
            break
        except:
            print("Invalid input. Age must be a whole number")

    client = Client(first_name, last_name, age)

    while True:
        try:
            num_haircuts = int(input("How many haircuts to add: "))
            break
        except:
            print("Invalid input. Must be a whole number.")

    for i in range(num_haircuts):
        print(f"\n Haircut {i +1}: ")
        raw_date = input("Enter the haircut date (mm-dd-yyyy): ")
        date = datetime.strptime(raw_date, "%m-%d-%Y")

        print("Enter haircut type: ")
        print("1 - Normal")
        print("2 - Special")
        choice = input("Enter your haircut type: ")

        if choice == "1":
            haircut_type = "Normal"
        else:
            haircut_type = "Special"

        while True:
            try:
                tip = float(input("Enter tip: "))
                break
            except:
                print("Invalid input. Please enter a number")

        print("Enter the stylist name \n")
        stylist_first = input("Stylist first name: ")
        stylist_last = input("Stylist last name: ")
        stylist = Stylist(stylist_first, stylist_last)

        haircut = Haircut(date, haircut_type, tip, stylist)

        client.haircuts.append(haircut)