import easygui
import os
import time
# Right click on import PIL to install it to your computer, so you can see
# the images
import PIL

burger_Combos = {
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
    combo_ID = easygui.enterbox("Enter Combo ID: ", "Adjuster "
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
    option = easygui.ynbox(f"Is the order correct?\n{combo_ID}\n{burger}: "
                           f"${burger_price}\n{side}: ${side_price}\n{drink}: "
                           f"${drink_price}\nTotal Price: $"
                           f"{total_price:.2f}", "Adjuster 9000", image=image)
    if option:
        pass
    else:
        add_combo()
    burger_Combos[combo_ID] = {}
    burger_Combos[combo_ID][burger] = burger_price
    burger_Combos[combo_ID][side] = side_price
    burger_Combos[combo_ID][drink] = drink_price


def change_combo():
    combo_list = []
    for i in burger_Combos:
        combo_list.append(i)
    option = easygui.buttonbox("What Combo would you like to change",
                               "Adjuster 9000", choices=combo_list,
                               image=image)
    combo_details_list = []
    keys = burger_Combos[option].keys()
    for e in keys:
        combo_details_list.append(e)
    option_2 = easygui.multchoicebox(f"What part of combo {option} would you "
                                     f"like to edit", "Adjuster 9000",
                                     choices=combo_details_list)
    for u in option_2:
        item = easygui.enterbox(f"Enter the name of the new item: ",
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
        del burger_Combos[option][u]
        burger_Combos[option][item] = item_price
    welcome()


def delete_combo():
    combo_list = []
    for i in burger_Combos:
        combo_list.append(i)
    option = easygui.multchoicebox("What Combo/s would you like to delete",
                                   "Adjuster 9000", choices=combo_list)
    for o in option:
        burger_Combos.pop(o)


def menu_print():
    print("=" * 20)
    for combo_id, combo_info in burger_Combos.items():
        print(f"\nCombo ID: {combo_id}")

        for key in combo_info:
            print(f"{key}: ${combo_info[key]:.2f}")
    print("=" * 20)


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