from turtle import Turtle, Screen
from random import choice

speed = list(range(1,11))
forward = list(range(1,21))
colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink",
     "gray", "brown", "cyan", "magenta",
    "lightblue", "lightgreen", "darkblue", "darkgreen"
]

Window = Screen()
Window.setup(width=1000)
Window.bgcolor("black")
Window.title("Turtles Race")
# Window.bye()

subscribers_list =[]
shared_color = []
name_list = []

def subscribers():
    global num 

    while True : 

        num = Window.textinput(prompt="What is the number of Subscribers? (Max five) ",title="Configurations")

        if num.isdigit() and int(num) <= 5: 
            num = int(num)
            break

    for i in range(num):
        chosen_color = choice(colors)
        colors.remove(chosen_color)

        sam = Turtle()
        sam.color(chosen_color)
        sam.shape("turtle")
        sam.penup()
        sam.goto(-480,y = -200+i*100 )
        shared_color.append(chosen_color)
        subscribers_list.append(sam)

def subs_name():
    for i in range(num):
        name = Window.textinput(prompt=f"Enter name of subscriber({i + 1})",title="Configurations").title()
        name_list.append(name)
        tom = Turtle()
        tom.penup()
        tom.hideturtle()
        tom.color(shared_color[i])
        tom.goto(-495,y = -188+i*100 )
        tom.write(f"{name} :) ",font=("arial",10,"bold"))

def move_turtles():
    race_in_progress = True
    rab3 = True
    while race_in_progress and rab3:
        race_in_progress = False  # Assume the race is over, will check for turtles still moving
        
        for sam in subscribers_list:
            if sam.xcor() < 480:  # If any turtle has not yet reached the finish line
                sam.speed(choice(speed))  
                sam.forward(choice(forward)) 
                
                if sam.xcor() >= 480 :
                    winner_index = subscribers_list.index(sam)
                    winner_name = name_list[winner_index]
                    winner_color = shared_color[winner_index]
                    Window.clear()
                    Window.bgcolor("black")

                    tim = Turtle()
                    tim.color(winner_color)
                    tim.penup()
                    tim.hideturtle()
                    tim.goto(x=0,y=0 )
                    tim.pendown()
                    tim.write(f"Congratulation, {winner_name}!",font=("arial",20,"bold"),align="center")  
                    rab3 = False
                race_in_progress = True

subscribers()
subs_name()
move_turtles()

Window.exitonclick()
