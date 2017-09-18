# Created by : Mr. Coxall
# Created on : 12-sep-2017
# Created for : ICS3U 
# Daily Assignment - Unit0-02 
# This program is the Calculator program, but with two eqautions

import ui

def equation1_touch_up_inside(sender):
    # displays the answer to equation1
    
    view['answer_label'].text = str(5*3)

def equation2_touch_up_inside(sender):
    # displays the answer to equation2
    
    view['answer_label'].text = str(5+5+3+3)
	
view = ui.load_view()
view.present('sheet')
