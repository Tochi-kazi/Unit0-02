# Created by : Tochukwu Iroakazi
# Created on : 26-sep-2017
# Created for : ICS3U 
# Daily Assignment - Unit1-05
# This program displays pizza cost

import ui

def calculate_button_touch_up_inside(sender):
    
    #input
    diameter= int(view['diameter_textbox'].text)
    
    #constant
    HST = 1.13
    
    #process
    cost = (1.75 + 0.5 * diameter) * HST
    
    #output
    view['cost_answer_label'].text = 'The cost is: ' + '${:,.2f}'.format(cost)
    
   

view = ui.load_view()
view.present('sheet')
