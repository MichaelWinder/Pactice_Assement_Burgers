import easygui
import os
import time
# Right click on import PIL to install it to your computer, so you can see
# the images
import PIL

burger_Combos = {
    "VALUE":
        {"Beef burger": "5.69",
         "Fries": "1.00",
         "Fizzy drink": "1.00"
         },
    "CHEEZY":
        {"Cheeseburger": "6.69",
         "Fries": "1.00",
         "Fizzy drink": "1.00"
         },
    "SUPER":
        {"Cheeseburger": "6.69",
         "Large fries": "2.00",
         "Smoothie": "2.00"
         }
}
image = os.environ['USERPROFILE'] + "\\Downloads\\Michael King.png"


def menu_print():
    print("="*20)
    for combo_id, combo_info in burger_Combos.items():
        print(f"\nCombo ID: {combo_id}")

        for key in combo_info:
            print(f"{key}: ${combo_info[key]:.2f}")
        total_price_list = []
        keys = burger_Combos[combo_id].keys()
        for e in keys:
            total_price_list.append(float(burger_Combos[combo_id][e]))
        print(f"The total cost for the {combo_id} combo is "
              f"${sum(total_price_list):.2f}")
    print("="*20)


def welcome():
    option = easygui.buttonbox("Welcome to Michael's Burger Menu Adjuster "
                               "9000!\n\nWhat would you like to do?",
                               "Adjuster 9000", image=image, choices=("Add "
                               "Combo", "Change Combo", "Delete Combo",
                               "Combo Menu", "Exit"))

    if option == "Add Combo":
        pass
    # add_Combo()
    elif option == "Change Combo":
        pass
    # change_Combo()
    elif option == "Delete Combo":
        pass
    # delete_Combo()
    elif option == "Combo Menu":
        time.sleep(0.5)
        menu_print()
    elif option == "Exit":
        pass


welcome()
