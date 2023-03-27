import easygui
import os
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
image = "\\Downloads\\Ethan Gamer.png"
user_profile = os.environ['USERPROFILE']
print(user_profile)
image2 = user_profile + image
easygui.msgbox(image=image2)
