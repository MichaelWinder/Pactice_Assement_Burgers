import easygui
import os
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
         "Large fries": "2",
         "Smoothie": "2"
         }
}
image = os.environ['USERPROFILE'] + "\\Downloads\\Michael King.png"


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
    # menu_print()
        pass
    elif option == "Exit":
        pass


welcome()
