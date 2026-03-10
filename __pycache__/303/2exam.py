# Mo Jansson
# IS 303 exam 2, working with classes, definitions, menus, and objects

from datetime import datetime

# First class to store info about a clinic employee
class Veterinarian:
    def __init__(self, first_name, last_name, specialty):
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.specialty = specialty


# A class to determine the visit details
class Visit:
    def __init__(self, date, visit_type, tip, vet):
        self.nicedate = date
        self.visit_type = visit_type
        self.tip = tip
        self.doctor = vet

        if visit_type == "Routine":
            self.fee = 50
        else:
            self.fee = 120

        self.total_cost = self.fee + self.tip


# Class to create pet information
class Pet:
    def __init__(self, name, species, age):
        self.name = name.upper()
        self.species = species.upper()
        self.age = age
        self.visits = []

    def print_visits(self):
        for visit in self.visits:
            print(f"Visit | Date: {visit.nicedate.strftime('%m-%d-%Y')} | Type: {visit.visit_type} "
                  f"| Cost: {visit.fee} | Tip: {visit.tip} | Total: {visit.total_cost} "
                  f"| Veterinarian: {visit.doctor.first_name} {visit.doctor.last_name}")


# Prints menu and returns user's choice
def display_Menu():
    print('--- Veterinarian Menu ---')
    print('1 - Add Pet and Visit')
    print('2 - Search for Pet')
    print('3 - Vet Totals (All Pets)')
    print('4 - Exit')
    return input("Choice: ")


# Receives pets list and prompts for pet information
def add_pet(pets):
    print("\n -- Add Pet --")

    name = input("Enter the pet's name: ")
    species = input("What kind of animal is your pet: ")

    while True:
        try:
            age = int(input("Enter the pet's age: "))
            break
        except:
            print("Invalid input. Age must be a whole number")

    pet = Pet(name, species, age)

    while True:
        try:
            num_visits = int(input("How many visits: "))
            break
        except:
            print("Invalid input. Must be a whole number.")

    for i in range(num_visits):

        print(f"\n Visit {i + 1}: ")

        raw_date = input("Enter the visit date (mm-dd-yyyy): ")
        date = datetime.strptime(raw_date, "%m-%d-%Y")

        print("Enter visit type:")
        print("1 - Routine")
        print("2 - Emergency")

        choice = input("Enter your visit type: ")

        if choice == "1":
            visit_type = "Routine"
        else:
            visit_type = "Emergency"

        while True:
            try:
                tip = float(input("Enter tip: "))
                break
            except:
                print("Invalid input. Tip must be a valid number")

        doctor_first = input("Please Enter the Vet's first name: ")
        doctor_last = input("Please Enter the Vet's last name: ")
        doctor_specialty = input("Please Enter the Vet's specialty: ")

        doctor = Veterinarian(doctor_first, doctor_last, doctor_specialty)

        visit = Visit(date, visit_type, tip, doctor)

        pet.visits.append(visit)

    pets.append(pet)


# Search for pet and print visit info
def search_pet(pets):
    print("\n -- Search for Pet --")

    name = input("Enter pet name: ").upper()
    species = input("Enter the species: ").upper()

    found = None

    for pet in pets:
        if pet.name == name and pet.species == species:
            found = pet
            break

    if found:
        print(f"\nPet: {found.name} | Species: {found.species} | Age: {found.age}")
        found.print_visits()
    else:
        print(f"\nNo pet found with the terms {name} {species}.")


# Calculates totals per veterinarian
def vet_totals(pets):

    print("\n -- Vet Totals (All Pets) --")

    totals = {}

    for pet in pets:
        for visit in pet.visits:

            vet_name = f"{visit.doctor.first_name} {visit.doctor.last_name}"

            if vet_name not in totals:
                totals[vet_name] = 0

            totals[vet_name] += visit.total_cost

    if totals:
        for vet_name in totals:
            print(f"{vet_name}: ${totals[vet_name]:.2f}")
    else:
        print("No visit data found.")


# Main program
bContinued = True
pets = []

while bContinued:

    choice = display_Menu()

    if choice == "1":
        add_pet(pets)

    elif choice == "2":
        search_pet(pets)

    elif choice == "3":
        vet_totals(pets)

    elif choice == "4":
        print("\nGoodbye from Paws & Care Clinic!")
        bContinued = False

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")