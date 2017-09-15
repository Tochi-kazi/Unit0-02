# Created by : Mr. Coxall
# Created on : 12-sep-2017
# Created for : ICS3U 
# Daily Assignment - Unit0-02 
# This program displays Hello World but in GUI

import ui

def hello_world_touch_up_inside (sender):
	print("Hello, World!")
	view['hello_world_label'].text = ("Hello, World!")
	
view = ui.load_view()
view.present('sheet')
