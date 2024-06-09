# Escaping the maze
# Project -06 

# turn_left(), front_is_clear(), at_goal(), move() ---> these are the in-built functions


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
    
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    