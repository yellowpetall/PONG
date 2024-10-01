from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def touched_paddle(self):
        self.bounce_x()
        if self.x_move < 0:
            self.x_move += -10
        else:
            self.x_move += 10

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move()

    def restart(self):
        self.hideturtle()
        self.goto(0, 0)
        if self.x_move < 0:
            self.x_move = 10
        else:
            self.x_move = -10
        self.showturtle()

    def stop(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
