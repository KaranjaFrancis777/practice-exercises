"""
def cook_ugali(water_cups,flour):
    water_cups = 2
    flour = 0.5
    print(F"cooking ugali with {water_cups} cups of water and {flour} kg of flour")


cook_ugali(4,2)

"""


def kugongewa(choice):
    if choice == "cheating":
        return "Unaweza_gongewa!"
    elif choice == "another boyfriend":
        return "hii imeenda."
    elif choice == "long weekend":
        return "Umegongewa!"
    elif choice == "sifeel poa":
        return "unagongewa!"
    elif choice == "babe am sorry simu ilikua imezima":
        return "maandishi haya si mageni jijini labda kwa mgeni jijini!!!"
    elif choice == "niko home":
        return "Utagongewa!"
    else:
        return "Invalid choice!"


# Prompt the user to make a choice
print("Enter a choice:")
options = ["cheating", "another boyfriend", "long weekend", "sifeel poa", "niko home",
           "babe am sorry simu ilikua imezima"]
print(", ".join(options))  # Display the options as a comma-separated string

user_choice = input("Make a choice: ")
result = kugongewa(user_choice)
print(result)
