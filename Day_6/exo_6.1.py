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


for i in range(6):
    move()
    jump()