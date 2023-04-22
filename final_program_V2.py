"""This program is a tool for digitally creating a menu of combos.

The combos consist of a Burger, Side, and a Drink. The program allows the
users to create combos, change combos, delete combos, and view the current menu
"""
import easygui
import os
import time
# Right click on import PIL to install it to your computer, so you can see
# the images
import PIL

# Main Dictionary
burger_combos = {
    "VALUE":
        {"Beef burger": 5.69,
         "Fries": 1.00,
         "Fizzy drink": 1.00
         },
    "CHEEZY":
        {"Cheeseburger": 6.69,
         "Fries": 1.00,
         "Fizzy drink": 1.00
         },
    "SUPER":
        {"Cheeseburger": 6.69,
         "Large fries": 2.00,
         "Smoothie": 2.00
         }
}
# To simplify the process of showing images
image = os.environ['USERPROFILE'] + "\\Downloads\\Michael King.png"


# Uses a series of easygui enter boxs to get the details from the user
# required to create a new combo. Then creates the new combo
def add_combo():
    """Add a combo to the Main Dictionary."""
    combo_id = easygui.enterbox("Enter Combo ID: ", "Adjuster "
                                                    "9000",
                                image=image).upper()
    burger = easygui.enterbox("Enter Burger: ", "Adjuster 9000",
                              image=image).capitalize()
    burger_price = easygui.enterbox(f"Enter Price for {burger}\nDon't use "
                                    f"$ sign", "Adjuster 9000", image=image)
    while True:
        try:
            burger_price = float(burger_price)
            break
        except ValueError:
            easygui.msgbox("Opps looks like your input wasn't a number\nTry "
                           "again", "Adjuster 9000", image=image)
            burger_price = easygui.enterbox(
                f"Enter Price for {burger}\nDon't use "
                f"$ sign", "Adjuster 9000", image=image)
    side = easygui.enterbox("Enter Side: ", "Adjuster 9000",
                            image=image).capitalize()
    side_price = easygui.enterbox(f"Enter Price for {side}\nDon't use "
                                  f"$ sign", "Adjuster 9000", image=image)
    while True:
        try:
            side_price = float(side_price)
            break
        except ValueError:
            easygui.msgbox("Opps looks like your input wasn't a number\nTry "
                           "again", "Adjuster 9000", image=image)
            side_price = easygui.enterbox(f"Enter Price for {side}\nDon't use "
                                          f"$ sign", "Adjuster 9000",
                                          image=image)
    drink = easygui.enterbox("Enter Drink: ", "Adjuster 9000",
                             image=image).capitalize()
    drink_price = easygui.enterbox(f"Enter Price for {drink}\nDon't use "
                                   f"$ sign", "Adjuster 9000", image=image)
    while True:
        try:
            drink_price = float(drink_price)
            break
        except ValueError:
            easygui.msgbox("Opps looks like your input wasn't a number\nTry "
                           "again", "Adjuster 9000", image=image)
            drink_price = easygui.enterbox(
                f"Enter Price for {drink}\nDon't use $ sign", "Adjuster 9000",
                image=image)
    total_price = burger_price + side_price + drink_price
    option = easygui.ynbox(f"Is the order correct?\n{combo_id}\n{burger}: "
                           f"${burger_price:.2f}\n{side}: ${side_price:.2f}"
                           f"\n{drink}: ${drink_price:.2f}\nTotal Price: $"
                           f"{total_price:.2f}", "Adjuster 9000", image=image)
    if option:
        pass
    else:
        add_combo()
    burger_combos[combo_id] = {}
    burger_combos[combo_id][burger] = burger_price
    burger_combos[combo_id][side] = side_price
    burger_combos[combo_id][drink] = drink_price


# Allows the user to change an already added combo
def change_combo():
    """Change an existing combo."""
    combo_list = []
    for i in burger_combos:
        combo_list.append(i)
    option = easygui.buttonbox("What Combo would you like to change",
                               "Adjuster 9000", choices=combo_list,
                               image=image)
    combo_details_list = []
    keys = burger_combos[option].keys()
    for e in keys:
        combo_details_list.append(e)
    option_2 = easygui.multchoicebox(f"What part of combo {option} would you "
                                     f"like to edit", "Adjuster 9000",
                                     choices=combo_details_list)
    for u in option_2:
        item = easygui.enterbox(f"Enter the name of the new {u}: ",
                                "Adjuster 9000", image=image).capitalize()
        item_price = easygui.enterbox(f"Enter Price for {item}\nDon't use "
                                      f"$ sign", "Adjuster 9000", image=image)
        while True:
            try:
                item_price = float(item_price)
                break
            except ValueError:
                easygui.msgbox(
                    "Opps looks like your input wasn't a number\nTry "
                    "again", "Adjuster 9000", image=image)
                item_price = easygui.enterbox(
                    f"Enter Price for {item}\n"
                    f"Don't use $ sign", "Adjuster 9000", image=image)
        del burger_combos[option][u]
        burger_combos[option][item] = item_price


# Deletes a combo of the user's choosing
def delete_combo():
    """Delete existing combo."""
    combo_list = []
    for i in burger_combos:
        combo_list.append(i)
    option = easygui.buttonbox("What Combo would you like to delete",
                               "Adjuster 9000", choices=combo_list,
                               image=image)
    del burger_combos[option]


# Prints out the current combo menu in the console
def menu_print():
    """Print entire combo menu."""
    print("=" * 20)
    for combo_id, combo_info in burger_combos.items():
        print(f"\nCombo ID: {combo_id}")

        for key in combo_info:
            print(f"{key}: ${combo_info[key]:.2f}")
        total_price_list = []
        keys = burger_combos[combo_id].keys()
        for e in keys:
            total_price_list.append(float(burger_combos[combo_id][e]))
        print(f"The total cost for the {combo_id} combo is "
              f"${sum(total_price_list):.2f}")
    print("=" * 20)


# Prints the final combo menu in the console and ends the program
def exit_program():
    """Exit the Program."""
    print(f"The final menu with {len(burger_combos)} combos")
    menu_print()
    quit()


# The core of the program that all other functions come back to. It directs
# the user to which ever function that is requested
def welcome():
    """Menu screen for navigating."""
    option = easygui.buttonbox("Welcome to Michael's Burger Menu Adjuster "
                               "9000!\n\nWhat would you like to do?",
                               "Adjuster 9000", image=image,
                               choices=("Add Combo", "Change Combo",
                                        "Delete Combo", "Combo Menu", "Exit"))

    if option == "Add Combo":
        add_combo()
    elif option == "Change Combo":
        change_combo()
    elif option == "Delete Combo":
        delete_combo()
    elif option == "Combo Menu":
        time.sleep(0.5)
        menu_print()
    elif option == "Exit":
        exit_program()


while True:
    welcome()
