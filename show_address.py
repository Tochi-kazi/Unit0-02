# Created by : Mr. Coxall
# Created on : 12-sep-2017
# Created for : ICS3U 
# Daily Assignment - Unit0-02 
# This program displays Hello World but in GUI

import ui

def show_address_touch_up_inside (sender):
	#print (Hello, World!) 
	view['name_label'].text = ("Tochukwu, Iroakazi!")
	view['city_label'].text = ('Ottawa')
	view['country_label']. text = ('Canada')
	
view = ui.load_view()
view.present('sheet')



