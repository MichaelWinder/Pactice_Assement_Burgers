import easygui
import os
import time
# Right click on import PIL to install it to your computer, so you can see
# the images
import PIL

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
image = os.environ['USERPROFILE'] + "\\Downloads\\Michael King.png"


def add_combo():
    combo_id = easygui.enterbox("Enter Combo ID: ", "Adjuster "
                                                    "9000",
                                image=image).upper()
    burger = easygui.enterbox("Enter Burger: ", "Adjuster 9000",
                              image=image).capitalize()
    burger_price = easygui.enterbox(f"Enter Price for {burger}\nDon't use "
                                    f"$ sign", "Adjuster 9000", image=image)
    side = easygui.enterbox("Enter Side: ", "Adjuster 9000",
                            image=image).capitalize()
    side_price = easygui.enterbox(f"Enter Price for {side}\nDon't use "
                                  f"$ sign", "Adjuster 9000", image=image)
    drink = easygui.enterbox("Enter Drink: ", "Adjuster 9000",
                             image=image).capitalize()
    drink_price = easygui.enterbox(f"Enter Price for {drink}\nDon't use "
                                   f"$ sign",
                                   "Adjuster 9000", image=image)
    burger_price = float(burger_price)
    side_price = float(side_price)
    drink_price = float(drink_price)
    total_price = burger_price + side_price + drink_price
    option = easygui.ynbox(f"Is the order correct?\n{combo_id}\n{burger}: "
                           f"${burger_price}\n{side}: ${side_price}\n{drink}: "
                           f"${drink_price}\nTotal Price: $"
                           f"{total_price:.2f}", "Adjuster 9000", image=image)
    if option:
        pass
    else:
        add_combo()
    burger_combos[combo_id] = {}
    burger_combos[combo_id][burger] = burger_price
    burger_combos[combo_id][side] = side_price
    burger_combos[combo_id][drink] = drink_price


def change_combo():
    combo_list = []
    for i in burger_combos:
        combo_list.append(i)
    option = easygui.buttonbox("What Combo would you like to change",
                               "Adjuster 9000", choices=combo_list,
                               image=image)
    burger_combos.pop(option)
    add_combo()


def delete_combo():
    combo_list = []
    for i in burger_combos:
        combo_list.append(i)
    option = easygui.multchoicebox("What Combo/s would you like to delete",
                                   "Adjuster 9000", choices=combo_list)
    for o in option:
        burger_combos.pop(o)


def menu_print():
    print("="*20)
    for combo_id, combo_info in burger_combos.items():
        print(f"\nCombo ID: {combo_id}")

        for key in combo_info:
            print(f"{key}: ${combo_info[key]}")
    print("="*20)


def welcome():
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
        quit()


while True:
    welcome()
