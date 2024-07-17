def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
        
## What the first loop will do is to loop and see if not at the goal, then checks if there is a wall in front of robot, then jump

## within the jump function, it will first turn left to face up and add a while loop to check for if there is a wall on the right and move() [Meaning as long as there is a wall on the right, it has to keep moving up {until when this condition of wall_on_right() is nolonger fulfilled ie false} then will jump onto the next line(11) which turns it right, then move one step, turns right]
## goes ahead to execute line 15, whre the condition front_of_the robot is clear (as long as its clear then the robot can keep moving) and if ts nolonger, the robot will turn left.
## After that the initial loop will be get to again and test if not at the goal continue to test if the wall is in front and jumps if not continues moving