from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_len=5)
        self.tilt(90)
        self.penup()
        self.goto(cords)
        self.color("white")


    def up(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor+20)

    def down(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor-20)