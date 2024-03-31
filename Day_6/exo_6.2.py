def go_top():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()


def go_down():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


def jump():
    go_top()
    move()
    go_down()


while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()