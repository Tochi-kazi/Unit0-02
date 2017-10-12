# Created by : Tochukwu Iroakazi
# Created on : 29-sep-2017
# Created for : ICS3UR-1 
# Daily Assignment - Unit3-03
# This program displays rock, paper and scissors game

import ui
import random 

number_to_guess = random.randint(1,3)
print(number_to_guess)

RO = 1
PAP = 2
SCI = 3

def Rock_button_touch_up_inside(sender):
    
    #process
    global number_to_guess
    if RO == number_to_guess:
        view['Check_label'].text = "Draw!"
     
    elif PAP == number_to_guess:
        view['Check_label'].text = "You lost!"
     
    else:
        view['Check_label'].text = "You won!"
    
def Paper_button_touch_up_inside(sender):
    
    global number_to_guess
    if number_to_guess == RO:
          view['Check_label'].text = "You won!"
     
    elif number_to_guess == PAP:
          view['Check_label'].text = "draw!"
     
    else: 
          view['Check_label'].text = "You lost!"


def Scissors_button_touch_up_inside(sender):
    
    global number_to_guess
    if number_to_guess == RO:
        view['Check_label'].text = "You lost!"
     
    elif number_to_guess == SCI:
          view['Check_label'].text = "draw!"
     
    else: 
          view['Check_label'].text = "You won!" 

view = ui.load_view()
view.present('full_screen')
