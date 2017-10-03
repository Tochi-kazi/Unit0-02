# Created by: Tochukwu Iroakazi
# Created on: 3 Oct 2016
# Created for: ICS3UR-1
# This program shows how to use an if statement in guess game

import ui

CORRECT_NUMBER = 5

def guess_number_touch_up_inside(sender):
    # check if the number is correct
    
    # input
    number_entered = int(view['guess_number_textfield'].text)
    
    # process
    if number_entered == CORRECT_NUMBER:
        # output
        view['answer_label'].text = "Correct!"
    

view = ui.load_view()
view.present('full_sheet')


