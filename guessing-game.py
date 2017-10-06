# Created by: Tochukwu Iroakazi
# Created on: 3 Oct 2016
# Created for: ICS3UR-1
# This program shows how to use an if statement in guess game

import ui
import random

# random number to guess
number_to_guess = random.randint(1,10)
print(number_to_guess)



def guess_number_touch_up_inside(sender):
    # check if the number is correct
    
    
    # input
    number_entered = int(view['guess_number_textfield'].text)
    
    # process
    global number_to_guess
    if number_entered == number_to_guess:
    
          # output
          view['answer_label'].text = "Correct!"
    
    else:
          view['answer_label'].text = "Sorry, that is wrong!"

view = ui.load_view()
view.present('full_sheet') 


