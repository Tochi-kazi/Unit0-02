# Created by : Tochukwu Iroakazi
# Created on : 21-sep-2017
# Created for : ICS3U 
# Daily Assignment - Unit1-03
# This program displays area and perimeter

import ui

def calculate_button_touch_up_inside(sender):
    #calculate area and perimeter
    
    #input
    lenght = int(view['lenght_textbox'].text)
    width = int(view['width_textbox'].text)
    
    #process
    area = lenght * width
    perimeter = 2 * (lenght + width)
    
    #output
    view['area_answer_label'].text = 'The area is: ' + str(area) + 'cm^2'
    view['perimeter_answer_label']. text = 'The perimeter is: ' + str(perimeter) + 'cm'

view = ui.load_view()
view.present('full_screen')
