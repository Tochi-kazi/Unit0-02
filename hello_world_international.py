# Created by : Mr. Coxall
# Created on : 12-sep-2017
# Created for : ICS3U 
# Daily Assignment - Unit0-02 
# This program is the Hello, World program, but with three bottums


import ui

def english_touch_up_inside(sender):
	# display the english version
	view['hello_world_label'].text = ('Hello, World!')
	
	
def french_touch_up_inside(sender):
	# display the french version
	view['hello_world_label'].text = ('Bonjour le monde!')

def spanish_touch_up_inside(sender):
	# displays the Spanish version
	view['hello_world_label'].text = ('Hola Mundo!')	

view = ui.load_view()
view.present('sheet')
