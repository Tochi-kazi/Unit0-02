# Created by : Tochukwu Iroakazi
# Created on : 25-sep-2017
# Created for : ICS3U 
# Daily Assignment - Unit1-04
# This program displays cicumference 

import ui

def calculate_button_touch_up_inside(sender):
    #calculate circumference
    
    #input
    radius = int(view['radius_textbox'].text)
    
    #constants
    PI = 3.14
    
    #process
    circumference = 2 * PI * radius
    
    #output
    view['circumference_answer_label'].text = 'The circumference is: ' + str(circumference) + 'cm'

view = ui.load_view()
view.present('sheet') 
