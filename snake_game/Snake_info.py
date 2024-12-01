from turtle import Turtle, Screen
from random import randint, uniform

window = Screen()
color = ["orange", "red", "cyan"]
         
class Snake:
    
    def __init__(self) -> None:
            self.snake_body = []
            self.place = 0
            self.body()
            self.head = self.snake_body[-1]

    def body(self):
          
          for i in range(3):
            sam = Turtle("square")
            sam.penup()
            sam.color(color[1])
            sam.goto(x=self.place,y=0)
            self.snake_body.append(sam)
            self.place += 20
          
    def extend(self):
          last_square = self.snake_body[0].pos()
          sam = Turtle("square")
          sam.penup()
          sam.color(color[1])
          sam.goto(last_square)
          self.snake_body.insert(0,sam)
         

    def move(self):
         for j in range(len(self.snake_body)-1):
              self.snake_body[j].goto(self.snake_body[j+1].pos())
         self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:  # Prevent going in the opposite direction
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

class Sec_Snak(Snake):
     def __init__(self) -> None:
          super().__init__()

     def body(self):
          for i in range(3):
            sam = Turtle("square")
            sam.penup()
            sam.color(color[0])
            sam.goto(x=self.place,y=100)
            self.snake_body.append(sam)
            self.place += 20

     def extend(self):
          last_square = self.snake_body[0].pos()
          sam = Turtle("square")
          sam.penup()
          sam.color(color[0])
          sam.goto(last_square)
          self.snake_body.insert(0,sam)

class Blue_Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(color[2])
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Make the food smaller
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        
        """Move the food to a new random location."""

        random_x = randint(-480, 480)
        random_y = randint(-300, 300)
        self.goto(random_x, random_y)


class White_Food(Blue_Food):
     def __init__(self):
          super().__init__()
          self.shape("circle")
          self.penup()
          self.color(color[1])
          self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Make the food smaller
          self.speed("fastest")
          self.refresh()

class Orange_Food(White_Food):
     def __init__(self):
          super().__init__()
          self.shape("circle")
          self.penup()
          self.color(color[0])
          self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Make the food smaller
          self.speed("fastest")
          self.refresh()

class Scoreboard:
     def __init__(self,player_name,player_color,player_position) :
          self.score = 0
          self.player_name = player_name
          self.player_color = player_color
          self.player_position = player_position
          self.text = Turtle()
          self.text.penup()
          self.text.hideturtle()
          self.text.color(player_color)
          self.update()

     def update(self):
          self.text.clear()
          self.text.goto(self.player_position)
          self.text.write(f"{self.player_name} Score: {self.score}", font=("arial", 10, "bold"))

     def increase(self):
          self.score += 1
          self.update()

          
class Winner(Blue_Food): 

     def __init__(self,shape_color):
          super().__init__()
          
          self.shape_color = shape_color
          self.color(self.shape_color)
          self.size = uniform(0.5,1)

          self.random_size()
     def random_size(self):
          self.shapesize(stretch_wid=self.size, stretch_len=self.size)


