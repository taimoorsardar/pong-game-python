from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.speed("slowest")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.TIMECONSTANT =0.1

    def move_ball(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def up_bounce(self):
        self.y_move = self.y_move*-1


    def down_bounce(self):
        self.x_move*=-1

    def reset_ball(self):
        self.goto(0,0)
        self.x_move *=-1
        self.TIMECONSTANT = 0.1