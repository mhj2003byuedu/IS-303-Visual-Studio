# Mo Jansson
# - Notes for new exam
# from datetime import datetime

# raw_date = input("enter the haircut date (mm-dd-yyyy): ")

# date = datetime.strptime(raw_date,"%m-%d-%Y").strptime

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

