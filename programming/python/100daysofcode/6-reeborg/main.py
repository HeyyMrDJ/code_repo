def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def check_front():
    while front_is_clear() == False:
        turn_right()
    if front_is_clear() == True:
        move()
    
def check_right():
    if wall_on_right() == False:
        turn_right()
    else:
        move()
        
def ai():
    if at_goal() == False:
        if front_is_clear() == True and right_is_clear() == False:
            move()
        if right_is_clear() and at_goal() == False:
            turn_right()
            move()
        else:
            turn_left()
        



ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
ai()
