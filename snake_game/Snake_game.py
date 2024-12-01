from Snake_info import *
from turtle import Screen
from time import sleep

window = Screen()
window.bgcolor("black")
window.setup(width=1000,height=700)
window.title("Snake Game")
window.tracer(0)

name_list = []
def config():
    subscriber = 0

    while subscriber < 2 :
        name = window.textinput(prompt=f"Enter name of subscriber({subscriber + 1})",title="Names").title()
        if not name : 
            return config()
        name_list.append(name)
        subscriber += 1

config()
white_board = Scoreboard(name_list[1],color[1],(-490, 310))
orange_board = Scoreboard(name_list[0],color[0],(-490, 330))


food_bl = Blue_Food()
food_wh = White_Food()
food_or = Orange_Food()
my_snake = Snake()
secondary_snake = Sec_Snak()

def disco(winner_name):
        window.tracer(0)
        if winner_name == "Tie" : 
            cellebration = Winner(color[2])
            cellebration.goto(0,0)
            cellebration.write(f"{winner_name} Game!", font=("arial", 25, "bold"),align="center")
        else:  
            for i in range(20): 
                    cellebration = Winner(color[name_list.index(winner_name)])
            cellebration.goto(0,0)
            cellebration.write(f" Congratulation {winner_name}!", font=("arial", 25, "bold"),align="center")
        window.update()


def wrap_around(snake):
    # Get the current position of the snake's head
    x, y = snake.head.xcor(), snake.head.ycor()
    
    # Check if the snake has moved out of the right side of the screen
    if x > 490:
        snake.head.setx(-490)
    
    # Check if the snake has moved out of the left side of the screen
    if x < -490:
        snake.head.setx(490)
    
    # Check if the snake has moved out of the top side of the screen
    if y > 340:
        snake.head.sety(-340)
    
    # Check if the snake has moved out of the bottom side of the screen
    if y < -340:
        snake.head.sety(340)


def check_collisions():

    if my_snake.head.distance(secondary_snake.head) < 10:
        return "Tie"
    # Check if the first snake collides with itself
    for segment in my_snake.snake_body[:-1]:  # Exclude the head
        if my_snake.head.distance(segment) < 10:
            return name_list[0]

    # Check if the second snake collides with itself
    for segment in secondary_snake.snake_body[:-1]:  # Exclude the head
        if secondary_snake.head.distance(segment) < 10:
            return name_list[1]

    # Check if the first snake's head collides with the second snake's body
    for segment in secondary_snake.snake_body:
        if my_snake.head.distance(segment) < 10:
            return name_list[0]

    # Check if the second snake's head collides with the first snake's body
    for segment in my_snake.snake_body:
        if secondary_snake.head.distance(segment) < 10:
            return name_list[1]

    return None

def eat():

    if my_snake.head.distance(food_bl) < 15 :
        food_bl.refresh()
        my_snake.extend()
        white_board.increase()

    elif my_snake.head.distance(food_wh) <15:
        my_snake.extend()
        food_wh.refresh()
        white_board.increase()

    elif secondary_snake.head.distance(food_bl) < 15 :
        food_bl.refresh()
        secondary_snake.extend()
        orange_board.increase()

    elif secondary_snake.head.distance(food_or) <15:
        food_or.refresh()
        secondary_snake.extend()
        orange_board.increase()

def setup_controls():
    """Set up the keybindings for both snakes."""
    # White snake controls
    window.onkey(my_snake.up, "Up")
    window.onkey(my_snake.down, "Down")
    window.onkey(my_snake.left, "Left")
    window.onkey(my_snake.right, "Right")

    # Orange snake controls
    window.onkey(secondary_snake.up, "w")
    window.onkey(secondary_snake.down, "s")
    window.onkey(secondary_snake.left, "a")
    window.onkey(secondary_snake.right, "d")

def exit_game():
    window.bye()

game_on = True

# Set up controls once before the game loop starts
setup_controls()
window.onkey(exit_game, "Escape")

while game_on:
    window.listen()  # Start listening for key inputs before the movement happens

    # Move and check secondary snake
    secondary_snake.move()  # Move secondary snake
    wrap_around(secondary_snake)  # Handle screen wrapping for secondary snake
    result = check_collisions()  # Check for collisions after the secondary snake moves
    my_snake.move()  # Move primary snake
    wrap_around(my_snake) 
    if result:  # If a collision is detected, stop the game
        window.clear()
        window.bgcolor("black")
        disco(result)
        sleep(3)
        game_on = False
    eat()

    # Update the window after all movements
    window.update()
    
    # Control the game speed
    sleep(0.07)








    