# Created by : Tochukwu Iroakazi
# Created on : 19-sep-2017
# Created for : ICS3U 
# Daily Assignment - Unit1-01 
# This program displays schools and masscots but in GUI

import ui

def mother_teresa_touch_up_inside (sender):
    #displays the school and masscot for MT
    view['school_label'].text = ('Mother teresa HS')
    view['mascot_label']. text = ('Titans')

def st_joe_touch_up_inside (sender):
    #displays the school amd masscot for St. joe
    view['school_label'].text = ('St.joe HS')
    view['mascot_label'].text = 'Jaguars'

def st_mark_touch_up_inside (sender):
    #displays the school and masscot for St. Mark HS
    view['school_label'].text = ('St.Marks HS')
    view['mascot_label']. text = ('Lions')

view = ui.load_view()
view.present('sheet')
