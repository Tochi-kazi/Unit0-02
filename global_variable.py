import ui

variableX = 25

def local_button_touch_up_inside(sender):
    # shows what happen with local variable
    
    variableX = 10
    variableY = 30
    variableZ = variableX + variableY
    
    view['local_answer_label'].text = str(variableZ)

def global_button_touch_up_inside(sender):
    #shows what happen with global variable
    
    #global variableX
    #variableX = variableX + 1
    variableY = 30
    variableZ = variableX + variableY
    
    view['global_answer_label'].text = str(variableZ)

view = ui.load_view()
view .present('sheet')
